import os
from keras.applications.inception_v3 import InceptionV3, preprocess_input
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD


# Initialize variables
batch_size = 128
train_dir = os.path.join(os.getcwd(), 'train_dir')
val_dir = os.path.join(os.getcwd(), 'val_dir')

# Create data generators
train_datagen =  ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
test_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(299, 299),
    batch_size=batch_size,
)
validation_generator = test_datagen.flow_from_directory(
    val_dir,
    target_size=(299, 299),
    batch_size=batch_size,
)

# Create model
base_model = InceptionV3(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(2, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

# Transfer learning
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Training
nb_train_samples = sum([len(files) for r, d, files in os.walk(train_dir)]) - 1
nb_val_samples = sum([len(files) for r, d, files in os.walk(val_dir)]) - 1

history = model.fit_generator(
    generator=train_generator,
    steps_per_epoch=nb_train_samples//batch_size,
    epochs=3,
    verbose=1,
    validation_data=validation_generator,
    validation_steps=nb_val_samples,
    class_weight='auto',
    workers=16)

model.save('inceptionv3-ft.model')
