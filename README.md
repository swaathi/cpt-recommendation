## Collaborative Filtering
Collaborative filtering produces recommendations based on the knowledge of users’ attitude to items, that is it uses the “wisdom of the crowd” to recommend items. In contrast, content-based recommender systems focus on the attributes of the items and give you recommendations based on the similarity between them.

In general, Collaborative filtering (CF) is the workhorse of recommender engines. The algorithm has a very interesting property of being able to do feature learning on its own, which means that it can start to learn for itself what features to use. CF can be divided into Memory-Based Collaborative Filtering and Model-Based Collaborative filtering.

Here we use Model-Based CF by using singular value decomposition (SVD) and Memory-Based CF by computing cosine similarity.

#### Memory-Based Collaborative Filtering

Memory-Based Collaborative Filtering approaches can be divided into two main sections: user-item filtering and item-item filtering. A user-item filtering will take a particular user, find users that are similar to that user based on similarity of ratings, and recommend items that those similar users liked. In contrast, item-item filtering will take an item, find users who liked that item, and find other items that those users or similar users also liked. It takes items and outputs other items as recommendations.

**Item-Item Collaborative Filtering:** “Users who liked this item also liked …”
**User-Item Collaborative Filtering:** “Users who are similar to you also liked …”

### Resources

- http://blog.ethanrosenthal.com/2015/11/02/intro-to-collaborative-filtering/
- http://online-dev.cambridgecoding.com/notebooks/eWReNYcAfB/implementing-your-own-recommender-systems-in-python-2
- **Interesting Read**: https://erikbern.com/2014/06/28/recurrent-neural-networks-for-collaborative-filtering/
- **Wiki**: https://en.wikipedia.org/wiki/Collaborative_filtering
