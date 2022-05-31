#!/usr/bin/env python
# coding: utf-8

# In[2]:


from keras.preprocessing.image import ImageDataGenerator


# # Image Data Augmentation

# In[3]:


train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)


# # Loading our data and performing data augmentation

# In[4]:


#performing data augmentation to train the data
x_train=train_datagen.flow_from_directory(r'C:\Users\Asmi Bhardwaj\Downloads\AI-Powered Nutrition Analyser for Fitness Enthusiasts\Dataset\TRAIN_SET',target_size=(64,64),batch_size=5,color_mode='rgb',class_mode='sparse')
#performing data augmentation to test the data
x_test=test_datagen.flow_from_directory(r'C:\Users\Asmi Bhardwaj\Downloads\AI-Powered Nutrition Analyser for Fitness Enthusiasts\Dataset\TEST_SET',target_size=(64,64),batch_size=5,color_mode='rgb',class_mode='sparse')


# In[5]:


print(x_train.class_indices)#checking the no. of classes


# In[6]:


from collections import Counter as c
c(x_train.labels)


# # Model Building

# In[7]:


###Importing Necessary Libraries


# In[8]:


import numpy as np


# In[9]:


import tensorflow


# In[10]:


from tensorflow.keras.models import Sequential


# In[11]:


from tensorflow.keras import layers


# In[12]:


from tensorflow.keras.layers import Dense,Flatten


# In[13]:


from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dropout


# In[14]:


from keras.preprocessing.image import ImageDataGenerator


# In[15]:


model=Sequential()


# In[16]:


###Creating the model


# In[17]:


classifier = Sequential()


# In[18]:


classifier.add(Conv2D(32, (3, 3), input_shape=(64,64,3),activation='relu'))


# In[19]:


classifier.add(MaxPooling2D(pool_size=(2,2)))


# In[20]:


classifier.add(Conv2D(32, (3,3),activation='relu'))


# In[21]:


classifier.add(MaxPooling2D(pool_size=(2,2)))


# In[22]:


classifier.add(Flatten())


# # Adding Dense Layers

# In[23]:


classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=5,activation='softmax'))


# In[24]:


classifier.summary()


# In[25]:


###Compiling the model


# In[26]:


classifier.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# # Training the model

# In[27]:


classifier.fit_generator(generator=x_train,steps_per_epoch = len(x_train),epochs=20,validation_data=x_test,validation_steps = len(x_test))


# In[28]:


###Saving our model


# In[29]:


classifier.save('nutrition.h5')


# In[30]:


###Predicting our results


# In[31]:


from tensorflow.keras.models import load_model
from keras.preprocessing import image
model = load_model("nutrition.h5")


# In[54]:


img = image.load_img(r"C:\Users\Asmi Bhardwaj\Downloads\AI-Powered Nutrition Analyser for Fitness Enthusiasts\Dataset\TEST_SET\APPLES\5_100.jpg", grayscale=False,target_size= (64,64))
x= image.img_to_array(img)
x= np.expand_dims(x,axis = 0)
pred=np.argmax(model.predict(x),axis=1)
pred


# In[55]:


index=['APPLES', 'BANANA', 'ORANGE', 'PINEAPPLE', 'WATERMELON']


# In[56]:


result=str(index[pred[0]])


# In[57]:


result


# In[ ]:




