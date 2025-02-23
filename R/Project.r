library("dbscan")
pdf("Dendogram.pdf")
dataPoints <- read.csv(file="Matrix.csv", header=FALSE, sep=",")
scaled.dataPoints <- scale(dataPoints)
cl <- hdbscan(t(scaled.dataPoints), minPts = 15)
plot(cl$hc, main="HDBSCAN* Hierarchy")
dev.off()