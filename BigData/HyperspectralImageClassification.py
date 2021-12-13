#Create CNN


#Prepare data


#Split train and test data


#Train the CNN model

#Plot graphs

#View Results as confusion matrix
mat = confusion_matrix(np.add(pred, 1), np.add(np.argmax(y_test, 1), 1))

df_cm = pd.DataFrame(mat, index = classes, columns = classes)

sns.heatmap(df_cm, annot=True, fmt='d')

plt.show()
