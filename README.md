# Customer Segmentation Analysis for Retail Strategy

This project performs customer segmentation analysis on the Online Retail dataset using RFM (Recency, Frequency, Monetary) analysis and various clustering techniques.

## Dataset
The analysis uses the Online Retail dataset from UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/352/online+retail

## Environment Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step-by-Step Setup Instructions

1. **Navigate to your project directory**
   ```bash
   cd /path/to/your/project
   ```

2. **Create the virtual environment**
   ```bash
   python3 -m venv find-cust-seg-env
   ```

3. **Activate the virtual environment**
   ```bash
   source find-cust-seg-env/bin/activate
   ```
   
   You should see `(find-cust-seg-env)` at the beginning of your terminal prompt, indicating the environment is active.

4. **Upgrade pip**
   ```bash
   pip install --upgrade pip
   ```

5. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

6. **Verify installation**
   ```bash
   python -c "import pandas, numpy, sklearn, matplotlib, seaborn, scipy; print('All packages installed successfully!')"
   ```

## Usage

### Activating the Environment
Each time you work on the project, activate the virtual environment:
```bash
source find-cust-seg-env/bin/activate
```

### Running the Analysis
1. Download the Online Retail dataset and place it in the same directory as the script
2. Run the analysis:
   ```bash
   python customer_segmentation.py
   ```

### Deactivating the Environment
When you're done working on the project:
```bash
deactivate
```

## Project Structure
```
project-directory/
├── README.md
├── requirements.txt
├── customer_segmentation.py
├── find-cust-seg-env/          # Virtual environment directory
└── Online Retail.csv           # Dataset (to be downloaded)
```

## Output Files
The analysis generates several output files:
- `customer_segments.csv`: Contains the RFM metrics and cluster assignments for each customer
- `silhouette_scores.png`: Plot showing the optimal number of clusters for K-means
- `dendrogram.png`: Hierarchical clustering dendrogram
- `cluster_characteristics.png`: Visualizations of cluster characteristics

## Analysis Components

### 1. Data Cleaning
- Removes missing values
- Handles negative quantities and prices
- Converts dates to proper format
- Calculates total transaction amounts

### 2. RFM Analysis
- **Recency**: Days since last purchase
- **Frequency**: Number of purchases
- **Monetary**: Total amount spent

### 3. Clustering Techniques
- **K-means clustering**: With automatic optimal cluster selection using silhouette score
- **Hierarchical clustering**: With dendrogram visualization using Ward linkage

### 4. Cluster Analysis
- Visualizes cluster characteristics
- Provides insights into customer segments
- Generates comprehensive reports

## Dendrogram Interpretation

### Understanding the Dendrogram
The dendrogram visualizes hierarchical clustering results showing how customers are grouped based on RFM similarity:

#### **Key Elements:**
- **Y-axis (Distance)**: Euclidean distance between clusters
- **X-axis**: Individual customers or clusters
- **Vertical lines**: Merge distance between clusters
- **Horizontal lines**: Cluster connections
- **Colors**: Different major customer segments

#### **Cluster Formation Process:**
1. **Bottom**: Individual customers start as separate clusters
2. **Middle**: Similar customers merge into sub-clusters
3. **Top**: All customers merge into one large cluster

### Optimal Number of Clusters

#### **2 Clusters (Distance ~10.5)**
- **Blue vs Green**: Two major customer segments
- **Use case**: High-level strategic decisions
- **Strategy**: Different approaches for each major segment

#### **3-4 Clusters (Distance ~4-6)**
- **Blue segment** + **Green sub-segments**
- **Use case**: Targeted marketing campaigns
- **Strategy**: Segment-specific marketing approaches

#### **6-8 Clusters (Distance ~2-3)**
- **Detailed segmentation** including tight sub-clusters
- **Use case**: Personalized marketing
- **Strategy**: Highly targeted, personalized campaigns

### Customer Segment Analysis

#### **High-Value, Loyal Customers (Blue Segment)**
- **Characteristics**: Similar RFM profiles, tight clustering
- **Strategy**: Premium services, loyalty programs
- **Marketing**: High-touch, personalized approach
- **Business Value**: Likely highest lifetime value

#### **Diverse Customer Base (Green Segment)**
- **Characteristics**: Varied RFM profiles, more spread out
- **Strategy**: Multiple marketing approaches, sub-segmentation
- **Marketing**: Different approaches for sub-groups
- **Business Value**: Potential for growth and optimization

#### **Tight Sub-Clusters (Orange)**
- **Characteristics**: Very similar RFM behavior
- **Strategy**: Group-specific promotions, referral programs
- **Marketing**: Community building, targeted content
- **Business Value**: Easy to target, high conversion potential

## Business Insights and Recommendations

### **Strategic Marketing Approaches**

#### **Segment 1: Premium Customers (Blue)**
```python
# Marketing Strategy
- VIP customer service
- Early access to new products
- Premium loyalty programs
- Personalized recommendations
- Exclusive events and offers
```

#### **Segment 2: Growth Customers (Green)**
```python
# Marketing Strategy
- Multiple touchpoint campaigns
- A/B testing different messages
- Graduated loyalty programs
- Cross-selling opportunities
- Re-engagement campaigns
```

#### **Sub-Segments: Niche Groups (Orange)**
```python
# Marketing Strategy
- Group-specific promotions
- Referral programs
- Community building
- Targeted content marketing
- Social media engagement
```

### **Implementation Guidelines**

1. **Start with 2-3 clusters** for initial strategy
2. **Refine to 6-8 clusters** for detailed targeting
3. **Monitor cluster evolution** over time
4. **Validate with business metrics** (revenue, retention)
5. **Iterate and optimize** based on results

## Technical Concepts

### **StandardScaler**
- Standardizes RFM features to mean=0, standard deviation=1
- Ensures all features contribute equally to clustering
- Essential for distance-based algorithms like K-means

### **Euclidean Distance**
- Measures straight-line distance between customer RFM profiles
- Used by both K-means and hierarchical clustering
- Requires standardized data for accurate results

### **Ward Linkage**
- Hierarchical clustering method that minimizes within-cluster variance
- Produces clusters of roughly equal size
- Good for customer segmentation applications

## Useful Commands

### Check installed packages
```bash
pip list
```

### Check Python location
```bash
which python
```

### Check environment status
```bash
echo $VIRTUAL_ENV
```

### Create Jupyter kernel
```bash
python -m ipykernel install --user --name=find-cust-seg-env --display-name="Customer Segmentation"
```

## Troubleshooting

### Common Issues and Solutions

1. **Permission errors**
   - Ensure you have write permissions in the directory
   - Try: `chmod +x setup_environment.sh` (if using setup script)

2. **Python not found**
   - Try using `python` instead of `python3`
   - Verify Python is installed: `python --version`

3. **Package installation errors**
   - Install packages one by one to identify problematic ones
   - Try: `pip install --upgrade setuptools` before installing other packages

4. **Virtual environment not activating**
   - Check if the environment directory exists
   - Verify the activation path is correct

5. **Style errors in matplotlib**
   - Update style names in the code to use newer versions
   - Use `plt.style.use('seaborn-v0_8')` instead of `plt.style.use('seaborn')`

6. **Excel file reading issues**
   - Ensure openpyxl is installed: `pip install openpyxl`
   - Check file format and encoding

## Dependencies
- pandas >= 2.2.0
- numpy >= 1.26.0
- scikit-learn >= 1.4.0
- matplotlib >= 3.8.0
- seaborn >= 0.13.0
- scipy >= 1.12.0
- openpyxl >= 3.1.0

## Contributing
Feel free to submit issues and enhancement requests!

## License
This project is for educational purposes as part of MSDS-555-1 Big Data Management & Analytics course. 