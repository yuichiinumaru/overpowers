# Auto-generated example usage from SKILL.md

# import deepchem as dc
#
# # Load CSV with SMILES
# featurizer = dc.feat.CircularFingerprint(radius=2, size=2048)
# loader = dc.data.CSVLoader(
#     tasks=['solubility', 'toxicity'],
#     feature_field='smiles',
#     featurizer=featurizer
# )
# dataset = loader.create_dataset('molecules.csv')
#
# # Load SDF files
# loader = dc.data.SDFLoader(tasks=['activity'], featurizer=featurizer)
# dataset = loader.create_dataset('compounds.sdf')
#
# # Load protein sequences
# loader = dc.data.FASTALoader()
# dataset = loader.create_dataset('proteins.fasta')

# # Fingerprints (for traditional ML)
# fp = dc.feat.CircularFingerprint(radius=2, size=2048)
#
# # Descriptors (for interpretable models)
# desc = dc.feat.RDKitDescriptors()
#
# # Graph features (for GNNs)
# graph_feat = dc.feat.MolGraphConvFeaturizer()
#
# # Apply featurization
# features = fp.featurize(['CCO', 'c1ccccc1'])

# # Scaffold splitting (recommended for molecules)
# splitter = dc.splits.ScaffoldSplitter()
# train, valid, test = splitter.train_valid_test_split(
#     dataset,
#     frac_train=0.8,
#     frac_valid=0.1,
#     frac_test=0.1
# )
#
# # Random splitting (for non-molecular data)
# splitter = dc.splits.RandomSplitter()
# train, test = splitter.train_test_split(dataset)
#
# # Stratified splitting (for imbalanced classification)
# splitter = dc.splits.RandomStratifiedSplitter()
# train, test = splitter.train_test_split(dataset)

# from sklearn.ensemble import RandomForestRegressor
#
# # Wrap scikit-learn model
# sklearn_model = RandomForestRegressor(n_estimators=100)
# model = dc.models.SklearnModel(model=sklearn_model)
# model.fit(train)

# # Multitask regressor (for fingerprints)
# model = dc.models.MultitaskRegressor(
#     n_tasks=2,
#     n_features=2048,
#     layer_sizes=[1000, 500],
#     dropouts=0.25,
#     learning_rate=0.001
# )
# model.fit(train, nb_epoch=50)

# # Graph Convolutional Network
# model = dc.models.GCNModel(
#     n_tasks=1,
#     mode='regression',
#     batch_size=128,
#     learning_rate=0.001
# )
# model.fit(train, nb_epoch=50)
#
# # Graph Attention Network
# model = dc.models.GATModel(n_tasks=1, mode='classification')
# model.fit(train, nb_epoch=50)
#
# # Attentive Fingerprint
# model = dc.models.AttentiveFPModel(n_tasks=1, mode='regression')
# model.fit(train, nb_epoch=50)

# # Load benchmark dataset
# tasks, datasets, transformers = dc.molnet.load_tox21(
#     featurizer='GraphConv',  # or 'ECFP', 'Weave', 'Raw'
#     splitter='scaffold',     # or 'random', 'stratified'
#     reload=False
# )
# train, valid, test = datasets
#
# # Train and evaluate
# model = dc.models.GCNModel(n_tasks=len(tasks), mode='classification')
# model.fit(train, nb_epoch=50)
#
# metric = dc.metrics.Metric(dc.metrics.roc_auc_score)
# test_score = model.evaluate(test, [metric])

# # ChemBERTa (BERT pretrained on 77M molecules)
# model = dc.models.HuggingFaceModel(
#     model='seyonec/ChemBERTa-zinc-base-v1',
#     task='classification',
#     n_tasks=1,
#     learning_rate=2e-5  # Lower LR for fine-tuning
# )
# model.fit(train, nb_epoch=10)
#
# # GROVER (graph transformer pretrained on 10M molecules)
# model = dc.models.GroverModel(
#     task='regression',
#     n_tasks=1
# )
# model.fit(train, nb_epoch=20)

# # Define metrics
# classification_metrics = [
#     dc.metrics.Metric(dc.metrics.roc_auc_score, name='ROC-AUC'),
#     dc.metrics.Metric(dc.metrics.accuracy_score, name='Accuracy'),
#     dc.metrics.Metric(dc.metrics.f1_score, name='F1')
# ]
#
# regression_metrics = [
#     dc.metrics.Metric(dc.metrics.r2_score, name='R²'),
#     dc.metrics.Metric(dc.metrics.mean_absolute_error, name='MAE'),
#     dc.metrics.Metric(dc.metrics.root_mean_squared_error, name='RMSE')
# ]
#
# # Evaluate
# train_scores = model.evaluate(train, classification_metrics)
# test_scores = model.evaluate(test, classification_metrics)

# # Predict on test set
# predictions = model.predict(test)
#
# # Predict on new molecules
# new_smiles = ['CCO', 'c1ccccc1', 'CC(C)O']
# new_features = featurizer.featurize(new_smiles)
# new_dataset = dc.data.NumpyDataset(X=new_features)
#
# # Apply same transformations as training
# for transformer in transformers:
#     new_dataset = transformer.transform(new_dataset)
#
# predictions = model.predict(new_dataset)

# import deepchem as dc
#
# # 1. Load benchmark
# tasks, datasets, _ = dc.molnet.load_bbbp(
#     featurizer='GraphConv',
#     splitter='scaffold'
# )
# train, valid, test = datasets
#
# # 2. Train model
# model = dc.models.GCNModel(n_tasks=len(tasks), mode='classification')
# model.fit(train, nb_epoch=50)
#
# # 3. Evaluate
# metric = dc.metrics.Metric(dc.metrics.roc_auc_score)
# test_score = model.evaluate(test, [metric])
# print(f"Test ROC-AUC: {test_score}")

# import deepchem as dc
#
# # 1. Load and featurize data
# featurizer = dc.feat.CircularFingerprint(radius=2, size=2048)
# loader = dc.data.CSVLoader(
#     tasks=['activity'],
#     feature_field='smiles',
#     featurizer=featurizer
# )
# dataset = loader.create_dataset('my_molecules.csv')
#
# # 2. Split data (use ScaffoldSplitter for molecules!)
# splitter = dc.splits.ScaffoldSplitter()
# train, valid, test = splitter.train_valid_test_split(dataset)
#
# # 3. Normalize (optional but recommended)
# transformers = [dc.trans.NormalizationTransformer(
#     transform_y=True, dataset=train
# )]
# for transformer in transformers:
#     train = transformer.transform(train)
#     valid = transformer.transform(valid)
#     test = transformer.transform(test)
#
# # 4. Train model
# model = dc.models.MultitaskRegressor(
#     n_tasks=1,
#     n_features=2048,
#     layer_sizes=[1000, 500],
#     dropouts=0.25
# )
# model.fit(train, nb_epoch=50)
#
# # 5. Evaluate
# metric = dc.metrics.Metric(dc.metrics.r2_score)
# test_score = model.evaluate(test, [metric])

# import deepchem as dc
#
# # 1. Load data (pretrained models often need raw SMILES)
# loader = dc.data.CSVLoader(
#     tasks=['activity'],
#     feature_field='smiles',
#     featurizer=dc.feat.DummyFeaturizer()  # Model handles featurization
# )
# dataset = loader.create_dataset('small_dataset.csv')
#
# # 2. Split data
# splitter = dc.splits.ScaffoldSplitter()
# train, test = splitter.train_test_split(dataset)
#
# # 3. Load pretrained model
# model = dc.models.HuggingFaceModel(
#     model='seyonec/ChemBERTa-zinc-base-v1',
#     task='classification',
#     n_tasks=1,
#     learning_rate=2e-5
# )
#
# # 4. Fine-tune
# model.fit(train, nb_epoch=10)
#
# # 5. Evaluate
# predictions = model.predict(test)

# # GOOD: Prevents data leakage
# splitter = dc.splits.ScaffoldSplitter()
# train, test = splitter.train_test_split(dataset)
#
# # BAD: Similar molecules in train and test
# splitter = dc.splits.RandomSplitter()
# train, test = splitter.train_test_split(dataset)

# transformers = [
#     dc.trans.NormalizationTransformer(
#         transform_y=True,  # Also normalize target values
#         dataset=train
#     )
# ]
# for transformer in transformers:
#     train = transformer.transform(train)
#     test = transformer.transform(test)

# # Option 1: Balancing transformer
# transformer = dc.trans.BalancingTransformer(dataset=train)
# train = transformer.transform(train)
#
# # Option 2: Use balanced metrics
# metric = dc.metrics.Metric(dc.metrics.balanced_accuracy_score)

# # Use DiskDataset for large datasets
# dataset = dc.data.DiskDataset.from_numpy(X, y, w, ids)
#
# # Use smaller batch sizes
# model = dc.models.GCNModel(batch_size=32)  # Instead of 128
