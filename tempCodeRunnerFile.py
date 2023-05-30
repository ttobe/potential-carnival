
# y_preds = xgb_wrapper.predict(x_test)
# y_pred_proba = xgb_wrapper.predict_proba(x_test)[:, 1]

# from sklearn.metrics import confusion_matrix, accuracy_score
# from sklearn.metrics import precision_score, recall_score
# from sklearn.metrics import f1_score, roc_auc_score

# # 수정된 get_clf_eval() 함수 
# def get_clf_eval(y_test, pred=None, pred_proba=None):
#     confusion = confusion_matrix( y_test, pred)
#     accuracy = accuracy_score(y_test , pred)
#     # ROC-AUC print 추가
#     print('정확도: {0:.4f}'.format(accuracy))
# get_clf_eval(y_test, y_preds, y_pred_proba)
