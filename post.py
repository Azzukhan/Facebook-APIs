#pip install facebook-sdk
import facebook

#Visit https://developers.facebook.com Create app
#goto to tool and select GraphAPI Explorer
# Give permission user_posts and generate access_token
# set the query path
#path-> user_ID_Post_ID?fields=comments.limit(1).summary(true),reactions.type(LIKE).limit(1).summary(true),shares.limit(1).summary(true),insights.limit(1).summary(true)

# copy perticular post id and also copy access_token

access_token = "access_token"

#authenticate GraphAPI through access_token
fb_post = facebook.GraphAPI(access_token)

#getting impression stats for mentioned post id.
impressions = fb_post.get_connections(
            id = "User_id_post_id",
            connection_name = "insights",
            metric = "post_activity",
            period = "lifetime",
            show_description_from_api_doc = True,
        )['data']

#getting number of shares for mentioned post id
shares = fb_post.get_object(
            id = "User_id_post_id",
            fields = 'shares')['shares']['count']

#fetching number of reactions of type LIKE for mentioned post id
likes = fb_post.get_connections(
            id = "User_id_post_id",
            connection_name = 'reactions',
            type = "LIKE",
            summary = 'true')['summary']["total_count"]

#fetching number of Comments for mentioned post id
comments = fb_post.get_connections(
            id = "User_id_post_id",
            connection_name = 'comments',
            summary = 'true')['summary']["total_count"]

# printing user_post like-shares, likes, comments and impressions
print("Shares", shares, "Likes:", likes, "Comments:", comments, "Impressions:",impressions)
