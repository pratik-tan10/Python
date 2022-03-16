# The mtcars dataset:
data <- as.matrix(mtcars)

# Default Heatmap
heatmap(data)

# No dendrogram nor reordering for neither column or row
heatmap(data, Colv = NA, Rowv = NA, scale="column")

# 1: native palette from R
heatmap(data, scale="column", col = cm.colors(256))
heatmap(data, scale="column", col = terrain.colors(256))
