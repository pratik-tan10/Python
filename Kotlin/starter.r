#matrices and data frames
my_vector <- 1:20
my_vector
dim(my_vector)
length(my_vector)
dim(my_vector) <- c(4,5)
dim(my_vector)
attributes(my_vector)
my_vector
class(my_vector)
my_matrix <- my_vector
?matrix
my_matrix2 <- matrix(1:20,4,5)
identical(my_matrix, my_matrix2)
patients <- c("Bill", "Gina","Kelly","Sean")
cbind(patients, my_matrix)
my_data <-data.frame(patients, my_matrix)
my_data
class(my_data)
cnames <- c("patient", "age", "weight", "bp", "rating", "test")
colnames(my_data) <- cnames
my_data
#Logic
TRUE == TRUE
(FALSE == TRUE) == FALSE
6==7
6<7
10<=10
5 != 7
!(5==7)

FALSE & FALSE
TRUE & c(TRUE, FALSE, FALSE)
TRUE && c(TRUE, FALSE, FALSE)

TRUE || c(TRUE, FALSE, FALSE)

5>8||6!=8&&4>3.9

isTRUE(6>4)
identical('twins','twins')

xor(5==6, !FALSE)
ints <- sample(10)
ints
ints>5
which(c(TRUE, FALSE, TRUE))
which(ints>7)
any(ints<0)
all(ints>0)
