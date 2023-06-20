def metodoQR(Matriz A, int n, float tol):
    Matriz P, Q, R, A_nova, A_velha, A_barra
    Vector lambda
    float val = 100

    P = I
    A_velha = A
    while (val > tol):
        (Q, R) = decomposicaoQR(A_velha, n)
        A_nova = R*Q
        A_velha = A_nova
        P = P*Q
        val = soma_dos_quadradros_dos_termos_abaixo_da_diagonal(A_nova, n)

    Lamb[1:n] = (A_nova)_i