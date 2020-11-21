---
theme: "Solarized"
transition: "slide"
slideNumber: true
---

<style type="text/css">
  .reveal h1,
  .reveal h2,
  .reveal h3,
  .reveal h4,
  .reveal h5,
  .reveal h6 {
    text-transform: none;
  }
</style>

# GeoPandas for Everyone 

----

### soupcurry049
2020-11-21 (Sat)

---

## あなたはだぁれ？

* 茶畑 (@soupcurry049)
* 経済学とか地理学 (GIS) やってました
* クラフトビールとスープカレーが好物

---

## GeoPandasとは

* その名の通りPandasの地理データ対応拡張

* データ構造としてPandasのSeries, DataFrameをベースとしたGeoSeries, GeoDataFrameを持つ


 
---

## できること

* geojsonやshapeファイルの読み書き

* 地図の作成

* 投影法の設定

* ジオプロセシング

* ジオコーディング

一通りの地理データハンドリングが可能

---

## ジオプロセシングの例: 
ディゾルブ

---

## ディゾルブとは

* 共通の属性を持つ地物をひとつの地物にまとめる

* 例: 同じ市に属する町丁目をまとめてその市の境界データを作る

* 欲しいスケールの境界データがない時には必須のジオプロセシング
---

GeoPandasを使うと簡単にできる  
例: 札幌市の行政区ごとの人口密度可視化


---

使うデータ:  
[e-Stat 国勢調査の境界データ(北海道全域)](https://www.e-stat.go.jp/gis/statmap-search?page=1&type=2&aggregateUnitForBoundary=A&toukeiCode=00200521&toukeiYear=2015&serveyId=A002005212015&prefCode=01&coordsys=1&format=shape)

---

シェープファイルの読み込み  
```python
import geopandas as gpd
hokkaido = gpd.read_file('data/h27ka01.shp')
type(hokkaido)
```

type()で見るとGeoDataFrameオブジェクトとして読み込まれているのが分かる

---

中身の確認
```python
display(hokkaido)
hokkaido.columns
```

geometryというカラムがあることでGeoDataFrameとして処理できる

---

地図としてプロット
```python
#プロット
hokkaido.plot()
#札幌市だけをプロット
sapporo = hokkaido[hokkaido.GST_NAME == '札幌市']
sapporo.plot()
```

---

ディゾルブによる区ごとの境界でコロプレス図作成
```python
sapporo_dissolved = sapporo.dissolve(by = 'CITY_NAME' aggfunc = 'sum')
sapporo_dissolved.plot()
sapporo_dissolved.loc[['中央区']].plot()
#人口密度コロプレス図の作成
sapporo_dissolved['DENSITY'] = 
sapporo_dissolved['JINKO'] / (sapporo_dissolved['AREA'] / (10**6))
sapporo_dissolved.plot(column = 'DENSITY', legend = True, cmap = 'YlOrRd')
```

---

* このようにGeoPandasのみでも簡単な地図作成は可能(色々やるにはmatplotlibも併用して)

* その他空間結合などのジオプロセシングも活用すれば快適なPython-GISライフ

* しかもQGISよりも処理が早い(らしい)ので是非使ってみてください！