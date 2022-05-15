from src.train_model import train_model
import pickle

def main():
    model = train_model()
    pickle.dump(model, open('iris_model.pkl', 'wb'))

if __name__ == '__main__':
    main()
