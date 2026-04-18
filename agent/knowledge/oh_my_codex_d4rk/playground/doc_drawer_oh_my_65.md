cores = model.predict_proba(X_test)[:, 1]
    else:
        scores = model.decision_function(X_test)

    predictions = model.predict(X_test)
    metrics = {
        "model": config.get("model"),
        "roc_auc": roc_auc_score(y_test, scores),
        "accuracy": accuracy_score(y_test, predictions),
    }
    print(json.dumps(metrics))


if __name__ == "__main__":
    main()