import geopandas as gpd

url = "https://plovput.li-st.net/getObjekti/"
# Citanje json file preko url-a i kreiranje geopandas dataframe-a
df = gpd.read_file(url)

# subselekcija dataframe-a pomocu boolean masking-a
df16 = df[df['tip_objekta']==16]

# Printanje broja objekata pod pretpostavkom da je svaki upis jedan objekt
print('\n\n')
print(f'Ukupno je zapisano {len(df)} objekata')
print(f'Od toga {len(df16)} objekata tipa 16\n\n')

# spremanje sub dataframe-a u geojson formatu
df16.to_file('tip16', driver="GeoJSON")