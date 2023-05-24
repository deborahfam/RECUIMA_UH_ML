from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, StackingClassifier
from sklearn.neural_network import MLPClassifier


# Load and split the data
# CAMBIAR POR EL DATA SET DE NOSOTROS
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42)

# Construct some pipelines
# Articulo ********Cardiovascular Disease Prediction by Machine Learning Algorithms Based on Cytokines in Kazakhs of China*********

pipe_art_9_2 = Pipeline([(('scl', StandardScaler())),
                         ('clf', LogisticRegression(random_state=42))])


pipe_art_9_5 = Pipeline([(('scl', StandardScaler())),
                         ('clf', svm.SVC(random_state=42))])


# Articulo 7 Use of Machine Learning Models to Predict Death After Acute Myocardial Infarction
# pipe_art_7_0 = Pipeline([(('scl', StandardScaler())),
#                          ('meta-cla', StackingClassifier(estimators=5, final_estimator=LogisticRegression()))])

# pipe_art_7_1 = Pipeline([(('scl', StandardScaler())),
#                          ('xbc', GradientBoostingClassifier(n_estimators=100, random_state=0))])

# # Articulo 1
# pipe_art_1_0 = Pipeline([(('scl', StandardScaler())),
#                          ('mlp', MLPClassifier(random_state=1, max_iter=300))])


# List of pipelines for ease of iteration
pipelines = [pipe_art_9_2, pipe_art_9_5,
             pipe_art_7_0, pipe_art_7_1, pipe_art_1_0]

# Dictionary of pipelines and classifier types for ease of reference
pipe_dict = {0: 'Logistic Regression', 1: 'Support Vector Machine',
             2: 'Meta-Classifier', 3: 'Ext-Grad-Boost', 4: 'MLP'}

# Fit the pipelines
for pipe in pipelines:
    pipe.fit(X_train, y_train)

# Compare accuracies
for idx, val in enumerate(pipelines):
    print('%s pipeline test accuracy: %.3f' %
          (pipe_dict[idx], val.score(X_test, y_test)))

# Identify the most accurate model on test data
best_acc = 0.0
best_clf = 0
best_pipe = ''
for idx, val in enumerate(pipelines):
    if val.score(X_test, y_test) > best_acc:
        best_acc = val.score(X_test, y_test)
        best_pipe = val
        best_clf = idx
print('Classifier with best accuracy: %s' % pipe_dict[best_clf])

# Save pipeline to file
joblib.dump(best_pipe, 'best_pipeline.pkl', compress=1)
print('Saved %s pipeline to file' % pipe_dict[best_clf])
