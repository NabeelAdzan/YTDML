class Comment:
    def __init__(self, vidid, text, like_amount, reply_amount):
        self.comment_text = text
        self.video_id = vidid
        self.likes = like_amount
        self.replies = reply_amount


class Video:
    def __init__(self, video_id, video_title, channel_name, cat_id, view_amount, likes_amount, dislikes_amount):
        self.id = video_id
        self.title = video_title
        self.channel = channel_name
        self.categoryid = cat_id
        self.views = view_amount
        self.likes = likes_amount
        self.dislikes = dislikes_amount
        self.ratio = self.get_ratio(likes_amount, dislikes_amount)

    def get_ratio(self, likes_amount, dislikes_amount):
        if int(likes_amount) > 0:
            if int(dislikes_amount) > 0:
                return int(likes_amount)/int(dislikes_amount)
            else:
                return "no dislikes"
        else:
            return "no likes"
