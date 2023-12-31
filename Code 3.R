P.data <- c(
  0.407407,
  0.120370,
  0.041667,
  0.092593,
  0.337963,
  0.438596,
  0.122807,
  0.035088,
  0.052632,
  0.350877,
  0.533333,
  0.133333,
  0,
  0.066667,
  0.266667,
  0.297872,
  0.063830,
  0.021277,
  0.085106,
  0.531915,
  0.453039,
  0.104972,
  0.016575,
  0.099448,
  0.325966
)

P <- matrix(P.data,nrow = 5, ncol = 5,byrow = TRUE)
print(P)

pi = matrix(
  c(0,0,0,0,1),
  nrow = 1,  
  ncol = 5,
  byrow = TRUE         
)

for (i in 1:10){
  
  pi <- pi %*% P
  
  if(i == 1){
    print("Π(1)")
    cat("\n")
    print(pi)
    cat("\n\n\n")
  }
  
  if(i == 5){
    print("Π(5)")
    cat("\n")
    print(pi)
    cat("\n\n\n")
  }
  
  if(i == 10){
    print("Π(10)")
    cat("\n")
    print(pi)
    cat("\n\n\n")
  }
  
}


