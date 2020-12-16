# Federated Learning
Federated learning (FL) is a machine learning technique that trains an algorithm across multiple decentralized edge devices or servers holding local data samples without exchanging them, offering advantages in **Scale, Privacy & Time**.

> - FL is an approach that downloads the current model and computes an updated model at the device itself using local data. These locally trained models are then sent from the devices back to the central server where they are aggregated and then a single consolidated and improved global model is sent back to the devices.
> - FL allows for machine learning algorithms to gain experience from a broad range of data sets located at different locations. The approach enables multiple organizations to collaborate on the development of models, but without needing to directly share secure data with each other.
> - FL decentralizes machine learning by removing the need to pool data into a single location. Instead, the model is trained in multiple iterations at different locations.

![Federated Model](https://blog.ml.cmu.edu/wp-content/uploads/2019/11/Screen-Shot-2019-11-12-at-10.41.38-AM-970x377.png)

### **[PySyft](https://github.com/OpenMined/PySyft)**. 
PySyft is a Python library to establish an API for secure and private Deep Learning that decouples private data from model training and let's us achieve Federated approach within the main Deep Learning frameworks like PyTorch and TensorFlow.

## Description
- **Experiment**: Traffic Data Projection
- **Aim**: Comparative Study of Models
- **Dataset**: GPS Logs

For more details, please visit respective jupyter notebooks.

