from sqlalchemy import create_engine
import pandas as pd

host = "localhost"
user = "root"
password = ""
database = "bd_biblioteca"

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{database}"
)

# conectando com o banco
try:
    df_usuarios = pd.read_sql("tb_usuarios", engine)
    df_livros = pd.read_sql("tb_livros", engine)
    df_alugados = pd.read_sql("tb_alugados", engine)
    df_itens_alugados = pd.read_sql("tb_itens_alugados", engine)

    # print(df_itens_alugados.head()) # teste de conexão
    
except Exception as e:
    print(f"Erro ao conectar ao banco.")
    
# juntando os dataframes
try: 
    df_merge1 = pd.merge(df_livros, df_itens_alugados, on="id_livro")
    df_merge2 = pd.merge(df_merge1, df_alugados, on="id_aluguel")
    df_merge_final = pd.merge(df_merge2, df_usuarios, on="id_usuario")
    
    # print(df_merge_final)
    
    filtro = (
        (df_merge_final["data_devolucao"] >= "2024-11-01") &
        (df_merge_final["data_devolucao"] <= "2024-11-30")
    )

    df_novembro = df_merge_final[filtro]
    print(
        df_novembro[[
            "id_usuario", "nome",
            "id_aluguel","data_aluguel", "data_devolucao", "valor",
            "id_livro","titulo"
            
        ]]
    )
    

except Exception as e:
    print(f"Erro no tratamendo dos dados {e}")