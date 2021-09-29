import csv
from classes import Comment
from classes import Video
from progress.bar import ChargingBar
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.neural_network import MLPClassifier
from functions import get_gaming_videos
from functions import get_entertainment_videos

category_id_dict = {
    "1": "Film and Animation",
    "2": "Autos and Vehicles",
    "10": "Music",
    "15": "Pets and Animals",
    "17": "Sports",
    "18": "Short Movies",
    "19": "Travel and Events",
    "20": "Gaming",
    "21": "Vlogging",
    "22": "People and Blogs",
    "23": "Comedy",
    "24": "Entertainment",
    "25": "News & Politics",
    "26": "Howto & Style",
    "27": "Education",
    "28": "Science & Technology",
    "29": "Nonprofits & Activism",
    "30": "Nonprofits & Activism",
    "31": "Anime/Animation",
    "32": "Action/Adventure",
    "33": "Classics",
    "34": "Comedy",
    "35": "Documentary",
    "36": "Drama",
    "37": "Family",
    "38": "Foreign",
    "39": "Horror",
    "40": "Sci-Fi/Fantasy",
    "41": "Thriller",
    "42": "Shorts",
    "43": "Shows",
    "44": "Trailers"
}

comments = "./data/UScomments.csv"
comments_len = 0
videos = "./data/USvideos.csv"
videos_len = 0

with open(comments) as csvfile:
    read = csv.reader(csvfile)
    times = 0
    for row in read:
        times += 1
    comments_len = times

with open(videos) as csvfile:
    read = csv.reader(csvfile)
    times = 0
    for row in read:
        times += 1
    videos_len = times

comments_list = []
videos_list = []

with open(comments) as csvfile:
    read = csv.reader(csvfile)
    times = 0
    pbar = ChargingBar('Processing Comment Dataset', max=comments_len)
    for row in read:
        if times != 0:
            comments_list.append(Comment(row[0], row[1], row[2], row[4]))
        times += 1
        pbar.next()
    print("\n" + str(times-1) + " comment dataset accounted." + "\n")

with open(videos) as csvfile:
    read = csv.reader(csvfile)
    times = 0
    pbar = ChargingBar('Processing Comment Dataset', max=videos_len)
    for row in read:
        if times != 0:
            videos_list.append(Video(row[0], row[1], row[2], row[3], row[5], row[6], row[7]))
        times += 1
        pbar.next()
    print("\n" + str(times-1) + " video dataset accounted." + "\n")

gaming_videos = get_gaming_videos(videos_list)
entertainment_videos = get_entertainment_videos(videos_list)

ml_mode = input("What do you want to do?\n1.Check Video Title Category\n2.Will this video title get views\n\n")
if ml_mode == "1":
    training, test = train_test_split(videos_list, test_size=0.01, random_state=42)

    cat_id_as_text_train = []
    for video in training:
        cat_id_as_text_train.append(category_id_dict[str(video.categoryid)])

    cat_id_as_text_test = []
    for video in test:
        cat_id_as_text_test.append(category_id_dict[str(video.categoryid)])

    train_x = [x.title for x in training]
    train_y = cat_id_as_text_train

    test_x = [x.title for x in test]
    test_y = cat_id_as_text_test

    vectorizer = CountVectorizer()

    train_x_vectors = vectorizer.fit_transform(train_x)

    test_x_vectors = vectorizer.transform(test_x)

    #SVC
    clf_svm = svm.SVC(kernel="linear")
    clf_svm.fit(train_x_vectors, train_y)

    clf_svm.predict(test_x_vectors)

    print("Score : " + str(clf_svm.score(test_x_vectors, test_y) * 100) + "%\n")

    yt_title_categories = True

    while yt_title_categories:
        test_set = []
        title = input("Name a title! (type exit to exit)\n")
        if title != "exit":
            test_set.append(title)
        else:
            break
        new_test = vectorizer.transform(test_set)

        print(clf_svm.predict(new_test))
elif ml_mode == "2":
    training, test = train_test_split(videos_list, test_size=0.01, random_state=42)

    viewsx = []
    viewsx2 = []

    for video in training:
        if int(video.views) < 1000:
            viewsx.append("F")
        elif int(video.views) < 10000:
            viewsx.append("D")
        elif int(video.views) < 50000:
            viewsx.append("C-")
        elif int(video.views) < 100000:
            viewsx.append("C+")
        elif int(video.views) < 250000:
            viewsx.append("B-")
        elif int(video.views) < 500000:
            viewsx.append("B")
        elif int(video.views) < 750000:
            viewsx.append("B+")
        elif int(video.views) < 1000000:
            viewsx.append("-A")
        elif int(video.views) < 1500000:
            viewsx.append("A")
        elif int(video.views) < 2000000:
            viewsx.append("A+")
        elif int(video.views) < 5000000:
            viewsx.append("S-")
        elif int(video.views) < 10000000:
            viewsx.append("S")
        elif int(video.views) < 20000000:
            viewsx.append("S+")
        else:
            viewsx.append("SSS")

    for video in test:
        if int(video.views) < 1000:
            viewsx2.append("F")
        elif int(video.views) < 10000:
            viewsx2.append("D")
        elif int(video.views) < 50000:
            viewsx2.append("C-")
        elif int(video.views) < 100000:
            viewsx2.append("C+")
        elif int(video.views) < 250000:
            viewsx2.append("B-")
        elif int(video.views) < 500000:
            viewsx2.append("B")
        elif int(video.views) < 750000:
            viewsx2.append("B+")
        elif int(video.views) < 1000000:
            viewsx2.append("-A")
        elif int(video.views) < 1500000:
            viewsx2.append("A")
        elif int(video.views) < 2000000:
            viewsx2.append("A+")
        elif int(video.views) < 5000000:
            viewsx2.append("S-")
        elif int(video.views) < 10000000:
            viewsx2.append("S-")
        elif int(video.views) < 10000000:
            viewsx2.append("S")
        elif int(video.views) < 20000000:
            viewsx2.append("S+")
        else:
            viewsx2.append("SSS")

    train_x = [x.title for x in training]
    train_y = viewsx

    test_x = [x.title for x in test]
    test_y = viewsx2

    vectorizer = CountVectorizer()

    train_x_vectors = vectorizer.fit_transform(train_x)

    test_x_vectors = vectorizer.transform(test_x)

    # Classification
    #clf_svm = svm.SVC(kernel="linear")
    #clf_svm.fit(train_x_vectors, train_y)
    #clf_svm.predict(test_x_vectors)

    clf = MLPClassifier()
    clf.fit(train_x_vectors, train_y)

    yt_title_categories = True

    while yt_title_categories:
        test_set = []
        title = input("Name a title! (type exit to exit)\n")
        if title != "exit":
            test_set.append(title)
        else:
            break
        new_test = vectorizer.transform(test_set)

        print(clf.predict(new_test))
