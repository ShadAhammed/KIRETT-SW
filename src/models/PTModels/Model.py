import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self, input_size):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_size, 20)
        self.dropout1 = nn.Dropout(0.1)

        self.fc2 = nn.Linear(20, 10)
        self.activation = nn.ReLU()
        self.dropout2 = nn.Dropout(0.1)

        self.fc3 = nn.Linear(10, 6)
        self.activation = nn.ReLU()
        self.dropout3 = nn.Dropout(0.1)

        self.fc4 = nn.Linear(6, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.dropout1(x)

        x = self.fc2(x)
        x = self.activation(x)
        x = self.dropout2(x)

        x = self.fc3(x)
        x = self.activation(x)
        x = self.dropout3(x)

        x = self.fc4(x)
        x = self.sigmoid(x)

        return x