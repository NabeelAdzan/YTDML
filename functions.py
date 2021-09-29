def get_gaming_videos(list_of_videos):
    gaming_videos_list = []
    for i in list_of_videos:
        if int(i.categoryid) == 20:
            gaming_videos_list.append(i)
        else:
            pass
    return gaming_videos_list


def get_entertainment_videos(list_of_videos):
    entertainment_videos_list = []
    for i in list_of_videos:
        if int(i.categoryid) == 24:
            entertainment_videos_list.append(i)
        else:
            pass
    return entertainment_videos_list
