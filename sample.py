#%%
import geopandas as gpd
# %%
#shapeファイルを読み込んでGeoDataFrameオブジェクトを生成
hokkaido = gpd.read_file('data/h27ka01.shp')
type(hokkaido)
# %%
#中身の確認
display(hokkaido)
hokkaido.columns
# %%
#プロット
hokkaido.plot()
# %%
#札幌市だけをプロット
sapporo = hokkaido[hokkaido.GST_NAME == '札幌市']
sapporo.plot()
# %%
#ディゾルブで行政区ごとに境界を結合
sapporo_dissolved = sapporo.dissolve(by = 'CITY_NAME', 
                                    aggfunc = 'sum')
sapporo_dissolved.plot()
sapporo_dissolved.loc[['中央区']].plot()
# %%
#人口密度コロプレス図の作成
sapporo_dissolved['DENSITY'] = sapporo_dissolved['JINKO'] / (sapporo_dissolved['AREA'] / (10**6))
sapporo_dissolved.plot(column = 'DENSITY', legend = True, cmap = 'YlOrRd')

# %%
