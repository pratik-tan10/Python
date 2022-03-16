# The mtcars dataset:
data <- as.matrix(mtcars)

# Default Heatmap
heatmap(data)

# No dendrogram nor reordering for neither column or row
heatmap(data, Colv = NA, Rowv = NA, scale="column")

# 1: native palette from R
heatmap(data, scale="column", col = cm.colors(256))
heatmap(data, scale="column", col = terrain.colors(256))

# 2: Rcolorbrewer palette
library(RColorBrewer)
coul <- colorRampPalette(brewer.pal(8, "PiYG"))(25)
heatmap(data, scale="column", col = coul)

# Add classic arguments like main title and axis title
heatmap(data, Colv = NA, Rowv = NA, scale="column", col = coul, xlab="variable", ylab="car", main="heatmap")

# Custom x and y labels with cexRow and labRow (col respectively)
heatmap(data, scale="column", cexRow=1.5, labRow=paste("new_", rownames(data),sep=""), col= colorRampPalette(brewer.pal(8, "Blues"))(25))

# Example: grouping from the first letter:
my_group <- as.numeric(as.factor(substr(rownames(data), 1 , 1)))
colSide <- brewer.pal(9, "Set1")[my_group]
colMain <- colorRampPalette(brewer.pal(8, "Blues"))(25)
heatmap(data, Colv = NA, Rowv = NA, scale="column" , RowSideColors=colSide, col=colMain   )
