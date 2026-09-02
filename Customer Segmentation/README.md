# Customer Segmentation

**Problem:** Identify customer segments with similar purchasing behaviors for personalized marketing strategies.

## Data
- **Source:** Mall Customers dataset (included: `mall_customers.csv`)
- **Size:** 200 customers, 5 variables
- **Features:** Age, gender, annual income, spending score

## Approach
- Exploratory analysis of spending and income patterns
- Elbow method to determine optimal number of clusters
- Baseline: K-means with k=3
- Improved: K-means with k=5 (optimal based on silhouette score)

## Results
- **Clusters identified:** 5 distinct segments
- **Silhouette Score:** ~0.50
- **Typical segments:** High/low income customers with high/low spending, enabling differentiated strategies

## How to Run

```bash
# Dataset included in repository
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook segmentacion_kmeans.ipynb
```

See: [`segmentacion_kmeans.ipynb`](./segmentacion_kmeans.ipynb)
