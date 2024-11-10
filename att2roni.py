import csv

def calcular_media_notas(arquivo_csv):
    with open(arquivo_csv, mode='r') as file:
        leitor = csv.reader(file)
        next(leitor) 
        notas = [float(linha[2]) for linha in leitor] 
        
    media = sum(notas) / len(notas) if notas else 0
    return media


arquivo_csv = 'C:/Users/hendryus/Downloads/alunos.csv'  
media = calcular_media_notas(arquivo_csv)

print(f'A média das notas é: {media:.2f}')
