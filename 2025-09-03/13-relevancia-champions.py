#IMPORTÂNCIA, RELEVÂNCIA DAS COLUNAS PARA SER "CHAMPIONS"
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coef': model.coef_[0]
}).sort_values(by='Coef', ascending=False)

print("Impacto das variáveis na probabilidade de ser Champion:")
print(coefficients)