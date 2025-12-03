print("Training meta-learner...")
meta_model = XGBClassifier(
    learning_rate=0.05,
    n_estimators=1000,
    max_depth=5,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric='auc',
    scale_pos_weight=1,
    random_state=42
)
meta_model.fit(meta_X, meta_y)
