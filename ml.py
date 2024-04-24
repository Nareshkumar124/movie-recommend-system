

def convertIntoObject():
    
    print("******************")
    import pandas as pd

    newDf=pd.read_csv("./Ready_to_use.csv")


    from sklearn.feature_extraction.text import CountVectorizer

    cv= CountVectorizer(max_features=5000,stop_words="english")

    vectors=cv.fit_transform(newDf["tags"])

    from sklearn.metrics.pairwise import cosine_similarity
    similarity=cosine_similarity(vectors)

    import pickle
    pickle.dump(newDf,open("movies.pkl","wb"))
    pickle.dump(similarity,open("similarity.pkl","wb"))
    

    