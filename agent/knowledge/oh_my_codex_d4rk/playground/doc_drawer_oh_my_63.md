):
    model_name = config.get("model", "decision_tree")
    params = dict(config.get("params", {}))

    if model_name == "decision_tree":
        return DecisionTreeClassifier(**params)
    if model_name == "random_forest":
        return RandomForestClassifier(**params)
    if model_name == "extra_trees":
        return ExtraTreesClassifier(**params)
    if model_name == "hist_gradient_boosting":
        return HistGradientBoostingClassifier(**params)
    if model_name == "logistic_regression":
        return make_pipeline(StandardScaler(), LogisticRegression(**params))

    raise ValueError(f"Unsupported model: {model_name}")