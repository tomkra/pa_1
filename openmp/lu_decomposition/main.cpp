#include <iostream>
#include <ctime>
#include <chrono>
#include <bits/stdc++.h>

using namespace std;
using namespace std::chrono;

const int SIZE = 3000;

void randomizeMatrixValues(double **matrix, int n) {
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++){
            matrix[i][j] = rand() % 10;
        }
    }
}

void print2DMatrix(double **matrix, int n) {
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void luDecomposition(double **matrix, int n) {
    std::chrono::high_resolution_clock::time_point start;
    std::chrono::high_resolution_clock::time_point end;
    int i, j, k;
    double sum=0;
    double **upper = new double*[n];
    double **lower = new double*[n];
    for(int i=0; i<n; i++) {
        upper[i] = new double[n];
        lower[i] = new double[n];
    }
    for(int i=0; i<n;i++)
        for(int j=0;j<n;j++) {
            upper[i][j] = 0;
            lower[i][j] = 0;
        }

    start = high_resolution_clock::now();
    #pragma omp parallel private(i,k,j, sum) shared(matrix, upper, lower)
    {
    for(i=0; i<n; i++){
        // U matrix
        #pragma omp for
        for(k=i; k<n; k++){
            sum = 0;
            for(j=0; j<i; j++){
                sum += (lower[i][j] * upper[j][k]);
            }
            upper[i][k] = matrix[i][k] - sum;
        }
        // L matrix
        #pragma omp for
        for(k=i; k<n; k++){
            if(i==k){
                lower[i][i] = 1;
            }else{
                sum = 0;
                for(j=0; j<i; j++){
                    sum += (lower[k][j] * upper[j][i]);
                }
                lower[k][i] = ((matrix[k][i] - sum) / upper[i][i]);
            }
        }
    }
    }

    end = high_resolution_clock::now();

    //print2DMatrix(matrix, n);
    //print2DMatrix(lower, n);
    //print2DMatrix(upper, n);
    cout << "LU decomposition duration(seconds): " << ((double) duration_cast<milliseconds>(end - start).count() / 1000) << " seconds." << endl;
}

int main()
{
    double** matrix = new double*[SIZE];
    for(int i=0; i<SIZE; i++)
        matrix[i] = new double[SIZE];

    randomizeMatrixValues(matrix, SIZE);
    luDecomposition(matrix, SIZE);

    return 0;
}
