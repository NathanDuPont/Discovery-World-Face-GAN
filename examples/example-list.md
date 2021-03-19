## Examples of GAN Facial Augmentation

---

### DC-GAN

[Medium Article](https://medium.com/using-deep-learning-dc-gan-to-add-featured-effect/recently-i-started-the-creative-applications-of-deep-learning-with-googles-tensorflow-of-parag-k-14453b215d2b)

[Source Code](https://github.com/Kjeanclaude/CADL-I-FinalPoject)

Notes: 

This GAN allows for adding and modifying features on an individuals face, but also has a blurring effect that removes lots of details from the end results. This may be good for testing, but for final implementation this might not work well.

### Transparent Latent GAN

[Medium Article](https://medium.com/p/d170b1b59255)

[Project Demo on Kaggle (broken)](https://www.kaggle.com/summitkwan/tl-gan-demo)

[Source Code](https://github.com/SummitKwan/transparent_latent_gan)

Notes: 
This network does a good job at producing realistic images, but currently only supports generating new faces from a random vector input. The accompanying articles provide good detail to describe modifications to latent vectors of faces within the model, and could be used with this model or others.

### Face Attribute Manipulation using GANs

[Towards Data Science Article](https://towardsdatascience.com/face-attribute-manipulation-using-gans-9fae92e9f1c3)

[Paper](https://arxiv.org/pdf/1612.05363.pdf)

[Source Code](https://github.com/MingtaoGuo/Learning-Residual-Images-for-Face-Attribute-Manipulation)


Notes: While this model can produce decent resolution outputs, there are lots of artifacts remaining from the original features and will likely not be usable in a final model. However, it does allow for modifying multiple different attributes with examples, and performance may be able to be boosted with modifications


### iSee - Removing glasses

[Article](https://blog.insightdatascience.com/isee-removing-eyeglasses-from-faces-using-deep-learning-d4e7d935376f#.v3iw0prqo)

Notes: This guide has lots of good information about developing these models from open-source code, but doesn't have as much code with the article

### Miscellaneous Articles
 
[Building Web Apps with PyTorch Models](https://medium.com/plotly/building-apps-for-editing-face-gans-with-dash-and-pytorch-hub-1e7026c0bc9a)