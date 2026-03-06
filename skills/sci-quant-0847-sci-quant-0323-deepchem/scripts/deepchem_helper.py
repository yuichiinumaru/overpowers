import sys

def train_multitask_regressor(train_dataset, nb_epoch=50):
    """
    Multitask regressor example.
    """
    import deepchem as dc
    model = dc.models.MultitaskRegressor(
        n_tasks=2,
        n_features=2048,
        layer_sizes=[1000, 500],
        dropouts=0.25,
        learning_rate=0.001
    )
    model.fit(train_dataset, nb_epoch=nb_epoch)
    return model

if __name__ == "__main__":
    print("Ready to train deepchem models.")
