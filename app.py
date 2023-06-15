import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit import components
import plotly.express as px
import plotly.graph_objects as go
plt.style.use('fivethirtyeight')

html_2023 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">22&nbsp;323&nbsp;843&nbsp;853,75</td><td style="text-align:right;">51&nbsp;412&nbsp;618&nbsp;343,17</td><td style="text-align:right;">18&nbsp;442&nbsp;933&nbsp;629,00</td><td style="text-align:right;">15&nbsp;297&nbsp;835&nbsp;516,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">21&nbsp;321&nbsp;275&nbsp;494,98</td><td style="text-align:right;">53&nbsp;154&nbsp;842&nbsp;440,69</td><td style="text-align:right;">15&nbsp;919&nbsp;168&nbsp;182,00</td><td style="text-align:right;">13&nbsp;357&nbsp;927&nbsp;312,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">23&nbsp;415&nbsp;993&nbsp;725,52</td><td style="text-align:right;">63&nbsp;960&nbsp;402&nbsp;421,10</td><td style="text-align:right;">20&nbsp;588&nbsp;052&nbsp;914,00</td><td style="text-align:right;">17&nbsp;338&nbsp;475&nbsp;865,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">19&nbsp;284&nbsp;075&nbsp;116,77</td><td style="text-align:right;">56&nbsp;188&nbsp;259&nbsp;181,06</td><td style="text-align:right;">15&nbsp;347&nbsp;610&nbsp;308,00</td><td style="text-align:right;">13&nbsp;898&nbsp;787&nbsp;066,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>9</td><td>September</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>11</td><td>November</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td><td style="text-align:right;"><i>belum rilis</i></td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:21:20 WIB</em></caption></table>'
html_2022 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">19&nbsp;173&nbsp;699&nbsp;043,36</td><td style="text-align:right;">27&nbsp;176&nbsp;531&nbsp;455,73</td><td style="text-align:right;">18&nbsp;211&nbsp;103&nbsp;488,00</td><td style="text-align:right;">12&nbsp;525&nbsp;388&nbsp;397,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">20&nbsp;472&nbsp;894&nbsp;279,18</td><td style="text-align:right;">44&nbsp;630&nbsp;366&nbsp;469,31</td><td style="text-align:right;">16&nbsp;638&nbsp;511&nbsp;813,00</td><td style="text-align:right;">13&nbsp;643&nbsp;754&nbsp;535,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">26&nbsp;497&nbsp;477&nbsp;726,13</td><td style="text-align:right;">61&nbsp;009&nbsp;058&nbsp;930,60</td><td style="text-align:right;">21&nbsp;962&nbsp;417&nbsp;654,00</td><td style="text-align:right;">17&nbsp;890&nbsp;856&nbsp;389,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">27&nbsp;322&nbsp;284&nbsp;675,60</td><td style="text-align:right;">55&nbsp;744&nbsp;554&nbsp;534,32</td><td style="text-align:right;">19&nbsp;757&nbsp;449&nbsp;353,00</td><td style="text-align:right;">15&nbsp;311&nbsp;997&nbsp;567,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">21&nbsp;509&nbsp;825&nbsp;822,05</td><td style="text-align:right;">51&nbsp;078&nbsp;811&nbsp;698,32</td><td style="text-align:right;">18&nbsp;609&nbsp;287&nbsp;096,00</td><td style="text-align:right;">13&nbsp;695&nbsp;896&nbsp;141,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">26&nbsp;150&nbsp;115&nbsp;171,99</td><td style="text-align:right;">55&nbsp;379&nbsp;269&nbsp;969,52</td><td style="text-align:right;">21&nbsp;003&nbsp;853&nbsp;585,00</td><td style="text-align:right;">15&nbsp;849&nbsp;221&nbsp;401,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">25&nbsp;563&nbsp;196&nbsp;494,36</td><td style="text-align:right;">58&nbsp;873&nbsp;597&nbsp;980,57</td><td style="text-align:right;">21&nbsp;345&nbsp;030&nbsp;399,00</td><td style="text-align:right;">15&nbsp;106&nbsp;273&nbsp;518,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">27&nbsp;862&nbsp;094&nbsp;370,64</td><td style="text-align:right;">59&nbsp;542&nbsp;590&nbsp;396,24</td><td style="text-align:right;">22&nbsp;150&nbsp;549&nbsp;517,00</td><td style="text-align:right;">16&nbsp;324&nbsp;740&nbsp;238,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">24&nbsp;777&nbsp;175&nbsp;554,39</td><td style="text-align:right;">60&nbsp;995&nbsp;692&nbsp;131,60</td><td style="text-align:right;">19&nbsp;808&nbsp;344&nbsp;348,00</td><td style="text-align:right;">15&nbsp;373&nbsp;240&nbsp;605,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">24&nbsp;728&nbsp;444&nbsp;384,48</td><td style="text-align:right;">60&nbsp;949&nbsp;225&nbsp;784,49</td><td style="text-align:right;">19&nbsp;135&nbsp;352&nbsp;916,00</td><td style="text-align:right;">15&nbsp;085&nbsp;178&nbsp;245,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">24&nbsp;094&nbsp;037&nbsp;088,31</td><td style="text-align:right;">57&nbsp;159&nbsp;651&nbsp;753,17</td><td style="text-align:right;">18&nbsp;962&nbsp;094&nbsp;932,00</td><td style="text-align:right;">14&nbsp;983&nbsp;782&nbsp;996,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">23&nbsp;827&nbsp;858&nbsp;043,97</td><td style="text-align:right;">54&nbsp;788&nbsp;095&nbsp;309,51</td><td style="text-align:right;">19&nbsp;863&nbsp;061&nbsp;497,00</td><td style="text-align:right;">17&nbsp;445&nbsp;166&nbsp;404,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:21:54 WIB</em></caption></table>'
html_2021 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">15&nbsp;300&nbsp;168&nbsp;401,83</td><td style="text-align:right;">52&nbsp;594&nbsp;533&nbsp;333,10</td><td style="text-align:right;">13&nbsp;329&nbsp;901&nbsp;020,00</td><td style="text-align:right;">13&nbsp;078&nbsp;332&nbsp;805,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">15&nbsp;255&nbsp;398&nbsp;398,45</td><td style="text-align:right;">47&nbsp;636&nbsp;989&nbsp;300,89</td><td style="text-align:right;">13&nbsp;264&nbsp;974&nbsp;634,00</td><td style="text-align:right;">12&nbsp;378&nbsp;562&nbsp;385,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">18&nbsp;398&nbsp;414&nbsp;762,13</td><td style="text-align:right;">50&nbsp;524&nbsp;633&nbsp;458,96</td><td style="text-align:right;">16&nbsp;787&nbsp;511&nbsp;490,00</td><td style="text-align:right;">17&nbsp;281&nbsp;282&nbsp;068,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">18&nbsp;474&nbsp;131&nbsp;706,88</td><td style="text-align:right;">49&nbsp;061&nbsp;313&nbsp;898,62</td><td style="text-align:right;">16&nbsp;204&nbsp;338&nbsp;764,00</td><td style="text-align:right;">15&nbsp;359&nbsp;269&nbsp;116,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">16&nbsp;908&nbsp;015&nbsp;508,43</td><td style="text-align:right;">51&nbsp;750&nbsp;618&nbsp;405,05</td><td style="text-align:right;">14&nbsp;234&nbsp;815&nbsp;276,00</td><td style="text-align:right;">14&nbsp;618&nbsp;029&nbsp;219,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">18&nbsp;547&nbsp;744&nbsp;863,51</td><td style="text-align:right;">52&nbsp;712&nbsp;714&nbsp;180,45</td><td style="text-align:right;">17&nbsp;218&nbsp;457&nbsp;483,00</td><td style="text-align:right;">15&nbsp;690&nbsp;996&nbsp;581,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">19&nbsp;369&nbsp;596&nbsp;670,95</td><td style="text-align:right;">55&nbsp;266&nbsp;605&nbsp;966,05</td><td style="text-align:right;">15&nbsp;263&nbsp;122&nbsp;650,00</td><td style="text-align:right;">13&nbsp;883&nbsp;775&nbsp;439,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">21&nbsp;443&nbsp;151&nbsp;840,86</td><td style="text-align:right;">54&nbsp;495&nbsp;451&nbsp;463,73</td><td style="text-align:right;">16&nbsp;678&nbsp;886&nbsp;850,00</td><td style="text-align:right;">14&nbsp;120&nbsp;443&nbsp;591,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">20&nbsp;618&nbsp;788&nbsp;618,10</td><td style="text-align:right;">50&nbsp;900&nbsp;622&nbsp;540,11</td><td style="text-align:right;">16&nbsp;234&nbsp;148&nbsp;586,00</td><td style="text-align:right;">14&nbsp;418&nbsp;830&nbsp;339,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">22&nbsp;090&nbsp;984&nbsp;014,33</td><td style="text-align:right;">56&nbsp;525&nbsp;781&nbsp;312,65</td><td style="text-align:right;">16&nbsp;293&nbsp;616&nbsp;090,00</td><td style="text-align:right;">14&nbsp;353&nbsp;729&nbsp;490,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">22&nbsp;845&nbsp;364&nbsp;125,29</td><td style="text-align:right;">50&nbsp;280&nbsp;024&nbsp;693,20</td><td style="text-align:right;">19&nbsp;328&nbsp;188&nbsp;076,00</td><td style="text-align:right;">15&nbsp;208&nbsp;908&nbsp;997,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">22&nbsp;357&nbsp;720&nbsp;667,68</td><td style="text-align:right;">49&nbsp;918&nbsp;547&nbsp;181,81</td><td style="text-align:right;">21&nbsp;352&nbsp;018&nbsp;156,00</td><td style="text-align:right;">17&nbsp;367&nbsp;172&nbsp;373,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:22:13 WIB</em></caption></table>'
html_2020 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">13&nbsp;636&nbsp;412&nbsp;653,62</td><td style="text-align:right;">50&nbsp;900&nbsp;144&nbsp;920,20</td><td style="text-align:right;">14&nbsp;268&nbsp;720&nbsp;284,00</td><td style="text-align:right;">12&nbsp;141&nbsp;682&nbsp;743,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">14&nbsp;042&nbsp;089&nbsp;243,23</td><td style="text-align:right;">49&nbsp;671&nbsp;209&nbsp;459,93</td><td style="text-align:right;">11&nbsp;548&nbsp;100&nbsp;132,00</td><td style="text-align:right;">13&nbsp;059&nbsp;584&nbsp;031,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">14&nbsp;031&nbsp;292&nbsp;077,89</td><td style="text-align:right;">54&nbsp;068&nbsp;776&nbsp;030,33</td><td style="text-align:right;">13&nbsp;352&nbsp;176&nbsp;374,00</td><td style="text-align:right;">14&nbsp;432&nbsp;183&nbsp;255,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">12&nbsp;159&nbsp;824&nbsp;545,01</td><td style="text-align:right;">45&nbsp;172&nbsp;672&nbsp;643,65</td><td style="text-align:right;">12&nbsp;535&nbsp;233&nbsp;221,00</td><td style="text-align:right;">15&nbsp;051&nbsp;046&nbsp;827,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">10&nbsp;452&nbsp;625&nbsp;424,79</td><td style="text-align:right;">42&nbsp;236&nbsp;217&nbsp;598,43</td><td style="text-align:right;">8&nbsp;438&nbsp;627&nbsp;383,00</td><td style="text-align:right;">10&nbsp;084&nbsp;426&nbsp;066,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">12&nbsp;006&nbsp;813&nbsp;612,70</td><td style="text-align:right;">46&nbsp;387&nbsp;784&nbsp;702,64</td><td style="text-align:right;">10&nbsp;760&nbsp;317&nbsp;981,00</td><td style="text-align:right;">11&nbsp;505&nbsp;323&nbsp;617,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">13&nbsp;689&nbsp;902&nbsp;558,81</td><td style="text-align:right;">46&nbsp;069&nbsp;923&nbsp;524,57</td><td style="text-align:right;">10&nbsp;464&nbsp;299&nbsp;676,00</td><td style="text-align:right;">11&nbsp;323&nbsp;464&nbsp;029,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">13&nbsp;055&nbsp;281&nbsp;120,71</td><td style="text-align:right;">43&nbsp;565&nbsp;183&nbsp;268,24</td><td style="text-align:right;">10&nbsp;742&nbsp;407&nbsp;847,00</td><td style="text-align:right;">11&nbsp;839&nbsp;690&nbsp;849,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">13&nbsp;956&nbsp;176&nbsp;571,88</td><td style="text-align:right;">43&nbsp;933&nbsp;093&nbsp;550,32</td><td style="text-align:right;">11&nbsp;570&nbsp;104&nbsp;770,00</td><td style="text-align:right;">12&nbsp;883&nbsp;228&nbsp;618,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">14&nbsp;363&nbsp;443&nbsp;251,43</td><td style="text-align:right;">47&nbsp;117&nbsp;842&nbsp;845,64</td><td style="text-align:right;">10&nbsp;786&nbsp;016&nbsp;684,00</td><td style="text-align:right;">12&nbsp;091&nbsp;546&nbsp;513,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">15&nbsp;258&nbsp;422&nbsp;043,10</td><td style="text-align:right;">53&nbsp;282&nbsp;636&nbsp;840,90</td><td style="text-align:right;">12&nbsp;664&nbsp;414&nbsp;194,00</td><td style="text-align:right;">12&nbsp;137&nbsp;149&nbsp;554,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">16&nbsp;539&nbsp;555&nbsp;059,63</td><td style="text-align:right;">57&nbsp;272&nbsp;738&nbsp;271,50</td><td style="text-align:right;">14&nbsp;438&nbsp;376&nbsp;084,00</td><td style="text-align:right;">15&nbsp;330&nbsp;669&nbsp;376,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:22:27 WIB</em></caption></table>'
html_2019 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">14&nbsp;028&nbsp;086&nbsp;397,26</td><td style="text-align:right;">55&nbsp;153&nbsp;741&nbsp;678,03</td><td style="text-align:right;">15&nbsp;005&nbsp;191&nbsp;440,00</td><td style="text-align:right;">13&nbsp;892&nbsp;230&nbsp;800,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">12&nbsp;788&nbsp;557&nbsp;131,66</td><td style="text-align:right;">48&nbsp;714&nbsp;544&nbsp;728,77</td><td style="text-align:right;">12&nbsp;465&nbsp;073&nbsp;944,00</td><td style="text-align:right;">12&nbsp;538&nbsp;456&nbsp;210,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">14&nbsp;447&nbsp;789&nbsp;013,35</td><td style="text-align:right;">57&nbsp;526&nbsp;309&nbsp;273,95</td><td style="text-align:right;">13&nbsp;746&nbsp;621&nbsp;857,00</td><td style="text-align:right;">13&nbsp;125&nbsp;266&nbsp;829,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">13&nbsp;068&nbsp;068&nbsp;332,92</td><td style="text-align:right;">52&nbsp;365&nbsp;329&nbsp;749,24</td><td style="text-align:right;">15&nbsp;399&nbsp;185&nbsp;930,00</td><td style="text-align:right;">14&nbsp;143&nbsp;962&nbsp;559,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">14&nbsp;751&nbsp;890&nbsp;717,71</td><td style="text-align:right;">57&nbsp;680&nbsp;016&nbsp;607,91</td><td style="text-align:right;">14&nbsp;606&nbsp;659&nbsp;275,00</td><td style="text-align:right;">14&nbsp;766&nbsp;069&nbsp;634,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">11&nbsp;763&nbsp;353&nbsp;136,51</td><td style="text-align:right;">46&nbsp;497&nbsp;604&nbsp;256,66</td><td style="text-align:right;">11&nbsp;495&nbsp;388&nbsp;062,00</td><td style="text-align:right;">10&nbsp;254&nbsp;928&nbsp;550,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">15&nbsp;238&nbsp;418&nbsp;109,04</td><td style="text-align:right;">56&nbsp;408&nbsp;079&nbsp;593,65</td><td style="text-align:right;">15&nbsp;518&nbsp;475&nbsp;622,00</td><td style="text-align:right;">13&nbsp;609&nbsp;908&nbsp;017,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">14&nbsp;261&nbsp;962&nbsp;733,89</td><td style="text-align:right;">52&nbsp;385&nbsp;275&nbsp;556,18</td><td style="text-align:right;">14&nbsp;169&nbsp;350&nbsp;761,00</td><td style="text-align:right;">12&nbsp;679&nbsp;655&nbsp;746,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">14&nbsp;080&nbsp;108&nbsp;446,19</td><td style="text-align:right;">54&nbsp;588&nbsp;169&nbsp;197,79</td><td style="text-align:right;">14&nbsp;263&nbsp;448&nbsp;876,00</td><td style="text-align:right;">13&nbsp;506&nbsp;445&nbsp;659,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">14&nbsp;881&nbsp;456&nbsp;853,91</td><td style="text-align:right;">61&nbsp;412&nbsp;977&nbsp;961,99</td><td style="text-align:right;">14&nbsp;759&nbsp;081&nbsp;430,00</td><td style="text-align:right;">13&nbsp;605&nbsp;297&nbsp;569,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">13&nbsp;944&nbsp;486&nbsp;956,68</td><td style="text-align:right;">56&nbsp;022&nbsp;187&nbsp;369,80</td><td style="text-align:right;">15&nbsp;340&nbsp;475&nbsp;284,00</td><td style="text-align:right;">16&nbsp;222&nbsp;862&nbsp;032,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">14&nbsp;428&nbsp;818&nbsp;305,10</td><td style="text-align:right;">55&nbsp;720&nbsp;138&nbsp;557,14</td><td style="text-align:right;">14&nbsp;506&nbsp;784&nbsp;516,00</td><td style="text-align:right;">14&nbsp;283&nbsp;648&nbsp;453,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:22:52 WIB</em></caption></table>'
html_2018 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">14&nbsp;576&nbsp;277&nbsp;325,78</td><td style="text-align:right;">48&nbsp;207&nbsp;188&nbsp;456,41</td><td style="text-align:right;">15&nbsp;309&nbsp;429&nbsp;258,00</td><td style="text-align:right;">13&nbsp;227&nbsp;092&nbsp;240,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">14&nbsp;132&nbsp;382&nbsp;055,93</td><td style="text-align:right;">46&nbsp;035&nbsp;282&nbsp;233,81</td><td style="text-align:right;">14&nbsp;185&nbsp;493&nbsp;772,00</td><td style="text-align:right;">13&nbsp;779&nbsp;364&nbsp;997,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">15&nbsp;510&nbsp;616&nbsp;703,18</td><td style="text-align:right;">52&nbsp;078&nbsp;259&nbsp;569,93</td><td style="text-align:right;">14&nbsp;463&nbsp;601&nbsp;047,00</td><td style="text-align:right;">12&nbsp;979&nbsp;524&nbsp;178,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">14&nbsp;496&nbsp;238&nbsp;057,47</td><td style="text-align:right;">47&nbsp;386&nbsp;767&nbsp;306,40</td><td style="text-align:right;">16&nbsp;162&nbsp;289&nbsp;358,00</td><td style="text-align:right;">14&nbsp;804&nbsp;211&nbsp;163,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">16&nbsp;198&nbsp;340&nbsp;826,26</td><td style="text-align:right;">51&nbsp;577&nbsp;563&nbsp;772,48</td><td style="text-align:right;">17&nbsp;662&nbsp;888&nbsp;974,00</td><td style="text-align:right;">16&nbsp;444&nbsp;214&nbsp;204,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">12&nbsp;941&nbsp;739&nbsp;831,72</td><td style="text-align:right;">49&nbsp;522&nbsp;181&nbsp;747,15</td><td style="text-align:right;">11&nbsp;267&nbsp;885&nbsp;237,00</td><td style="text-align:right;">10&nbsp;277&nbsp;766&nbsp;719,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">16&nbsp;284&nbsp;719&nbsp;992,31</td><td style="text-align:right;">54&nbsp;441&nbsp;268&nbsp;184,18</td><td style="text-align:right;">18&nbsp;297&nbsp;145&nbsp;166,00</td><td style="text-align:right;">15&nbsp;532&nbsp;866&nbsp;751,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">15&nbsp;865&nbsp;124&nbsp;056,42</td><td style="text-align:right;">48&nbsp;619&nbsp;406&nbsp;722,60</td><td style="text-align:right;">16&nbsp;818&nbsp;139&nbsp;736,37</td><td style="text-align:right;">15&nbsp;554&nbsp;819&nbsp;747,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">14&nbsp;956&nbsp;348&nbsp;234,23</td><td style="text-align:right;">50&nbsp;393&nbsp;032&nbsp;873,86</td><td style="text-align:right;">14&nbsp;610&nbsp;057&nbsp;878,00</td><td style="text-align:right;">12&nbsp;860&nbsp;756&nbsp;790,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">15&nbsp;909&nbsp;072&nbsp;846,28</td><td style="text-align:right;">56&nbsp;706&nbsp;511&nbsp;181,50</td><td style="text-align:right;">17&nbsp;667&nbsp;618&nbsp;898,00</td><td style="text-align:right;">15&nbsp;923&nbsp;155&nbsp;505,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">14&nbsp;851&nbsp;720&nbsp;862,22</td><td style="text-align:right;">51&nbsp;141&nbsp;321&nbsp;156,80</td><td style="text-align:right;">16&nbsp;901&nbsp;814&nbsp;777,00</td><td style="text-align:right;">15&nbsp;618&nbsp;755&nbsp;159,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">14&nbsp;290&nbsp;093&nbsp;210,17</td><td style="text-align:right;">52&nbsp;798&nbsp;736&nbsp;010,76</td><td style="text-align:right;">15&nbsp;364&nbsp;986&nbsp;090,00</td><td style="text-align:right;">14&nbsp;716&nbsp;898&nbsp;033,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:23:06 WIB</em></caption></table>'
html_2017 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">13&nbsp;397&nbsp;676&nbsp;587,81</td><td style="text-align:right;">43&nbsp;565&nbsp;989&nbsp;974,33</td><td style="text-align:right;">11&nbsp;973&nbsp;765&nbsp;825,00</td><td style="text-align:right;">11&nbsp;677&nbsp;887&nbsp;405,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">12&nbsp;615&nbsp;980&nbsp;315,09</td><td style="text-align:right;">37&nbsp;467&nbsp;812&nbsp;722,18</td><td style="text-align:right;">11&nbsp;359&nbsp;410&nbsp;570,00</td><td style="text-align:right;">12&nbsp;640&nbsp;301&nbsp;805,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">14&nbsp;718&nbsp;477&nbsp;686,88</td><td style="text-align:right;">47&nbsp;776&nbsp;913&nbsp;741,86</td><td style="text-align:right;">13&nbsp;283&nbsp;186&nbsp;576,00</td><td style="text-align:right;">13&nbsp;474&nbsp;016&nbsp;869,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">13&nbsp;269&nbsp;689&nbsp;617,58</td><td style="text-align:right;">44&nbsp;248&nbsp;565&nbsp;280,56</td><td style="text-align:right;">11&nbsp;950&nbsp;612&nbsp;898,00</td><td style="text-align:right;">12&nbsp;432&nbsp;054&nbsp;822,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">14&nbsp;333&nbsp;859&nbsp;523,55</td><td style="text-align:right;">44&nbsp;049&nbsp;700&nbsp;226,86</td><td style="text-align:right;">13&nbsp;772&nbsp;553&nbsp;263,00</td><td style="text-align:right;">14&nbsp;996&nbsp;662&nbsp;995,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">11&nbsp;661&nbsp;376&nbsp;380,86</td><td style="text-align:right;">39&nbsp;899&nbsp;123&nbsp;547,30</td><td style="text-align:right;">9&nbsp;991&nbsp;567&nbsp;566,00</td><td style="text-align:right;">11&nbsp;067&nbsp;266&nbsp;662,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">13&nbsp;611&nbsp;062&nbsp;499,27</td><td style="text-align:right;">45&nbsp;104&nbsp;086&nbsp;462,25</td><td style="text-align:right;">13&nbsp;889&nbsp;809&nbsp;439,00</td><td style="text-align:right;">13&nbsp;474&nbsp;009&nbsp;387,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">15&nbsp;187&nbsp;990&nbsp;996,89</td><td style="text-align:right;">47&nbsp;603&nbsp;859&nbsp;326,86</td><td style="text-align:right;">13&nbsp;509&nbsp;196&nbsp;595,00</td><td style="text-align:right;">14&nbsp;290&nbsp;326&nbsp;822,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">14&nbsp;580&nbsp;216&nbsp;111,80</td><td style="text-align:right;">48&nbsp;289&nbsp;451&nbsp;395,64</td><td style="text-align:right;">12&nbsp;788&nbsp;291&nbsp;967,00</td><td style="text-align:right;">13&nbsp;017&nbsp;265&nbsp;351,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">15&nbsp;252&nbsp;563&nbsp;526,06</td><td style="text-align:right;">50&nbsp;820&nbsp;828&nbsp;191,65</td><td style="text-align:right;">14&nbsp;249&nbsp;179&nbsp;382,00</td><td style="text-align:right;">14&nbsp;703&nbsp;970&nbsp;178,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">15&nbsp;334&nbsp;735&nbsp;600,61</td><td style="text-align:right;">47&nbsp;905&nbsp;955&nbsp;325,27</td><td style="text-align:right;">15&nbsp;113&nbsp;523&nbsp;078,00</td><td style="text-align:right;">14&nbsp;557&nbsp;794&nbsp;980,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">14&nbsp;864&nbsp;547&nbsp;089,62</td><td style="text-align:right;">49&nbsp;114&nbsp;346&nbsp;862,32</td><td style="text-align:right;">15&nbsp;104&nbsp;466&nbsp;563,00</td><td style="text-align:right;">14&nbsp;417&nbsp;729&nbsp;365,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:28:54 WIB</em></caption></table>'
html_2016 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">10&nbsp;581&nbsp;883&nbsp;837,98</td><td style="text-align:right;">39&nbsp;593&nbsp;480&nbsp;160,23</td><td style="text-align:right;">10&nbsp;466&nbsp;995&nbsp;371,00</td><td style="text-align:right;">11&nbsp;170&nbsp;356&nbsp;250,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">11&nbsp;316&nbsp;734&nbsp;188,51</td><td style="text-align:right;">38&nbsp;699&nbsp;176&nbsp;125,86</td><td style="text-align:right;">10&nbsp;175&nbsp;631&nbsp;438,00</td><td style="text-align:right;">12&nbsp;777&nbsp;162&nbsp;927,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">11&nbsp;812&nbsp;127&nbsp;477,93</td><td style="text-align:right;">43&nbsp;029&nbsp;049&nbsp;633,14</td><td style="text-align:right;">11&nbsp;301&nbsp;709&nbsp;941,00</td><td style="text-align:right;">14&nbsp;280&nbsp;888&nbsp;506,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">11&nbsp;689&nbsp;745&nbsp;851,03</td><td style="text-align:right;">39&nbsp;558&nbsp;381&nbsp;868,75</td><td style="text-align:right;">10&nbsp;813&nbsp;624&nbsp;836,00</td><td style="text-align:right;">12&nbsp;028&nbsp;222&nbsp;569,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">11&nbsp;517&nbsp;409&nbsp;125,88</td><td style="text-align:right;">40&nbsp;622&nbsp;406&nbsp;240,97</td><td style="text-align:right;">11&nbsp;140&nbsp;679&nbsp;613,00</td><td style="text-align:right;">13&nbsp;132&nbsp;879&nbsp;687,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">13&nbsp;206&nbsp;122&nbsp;765,22</td><td style="text-align:right;">44&nbsp;766&nbsp;894&nbsp;584,67</td><td style="text-align:right;">12&nbsp;095&nbsp;220&nbsp;496,00</td><td style="text-align:right;">13&nbsp;501&nbsp;715&nbsp;838,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">9&nbsp;649&nbsp;503&nbsp;975,97</td><td style="text-align:right;">39&nbsp;032&nbsp;046&nbsp;988,71</td><td style="text-align:right;">9&nbsp;017&nbsp;159&nbsp;102,00</td><td style="text-align:right;">10&nbsp;138&nbsp;881&nbsp;648,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">12&nbsp;753&nbsp;921&nbsp;321,13</td><td style="text-align:right;">45&nbsp;800&nbsp;576&nbsp;791,74</td><td style="text-align:right;">12&nbsp;385&nbsp;153&nbsp;588,00</td><td style="text-align:right;">14&nbsp;001&nbsp;735&nbsp;399,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">12&nbsp;579&nbsp;750&nbsp;249,95</td><td style="text-align:right;">44&nbsp;146&nbsp;271&nbsp;670,66</td><td style="text-align:right;">11&nbsp;297&nbsp;511&nbsp;237,00</td><td style="text-align:right;">12&nbsp;809&nbsp;168&nbsp;012,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">12&nbsp;743&nbsp;736&nbsp;883,73</td><td style="text-align:right;">47&nbsp;378&nbsp;384&nbsp;671,57</td><td style="text-align:right;">11&nbsp;507&nbsp;180&nbsp;543,00</td><td style="text-align:right;">12&nbsp;391&nbsp;159&nbsp;183,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">13&nbsp;502&nbsp;920&nbsp;382,69</td><td style="text-align:right;">46&nbsp;606&nbsp;206&nbsp;087,95</td><td style="text-align:right;">12&nbsp;669&nbsp;434&nbsp;720,00</td><td style="text-align:right;">12&nbsp;804&nbsp;703&nbsp;935,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">13&nbsp;832&nbsp;355&nbsp;186,41</td><td style="text-align:right;">45&nbsp;551&nbsp;700&nbsp;747,95</td><td style="text-align:right;">12&nbsp;782&nbsp;515&nbsp;616,00</td><td style="text-align:right;">12&nbsp;988&nbsp;497&nbsp;126,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:29:12 WIB</em></caption></table>'
html_2015 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">13&nbsp;244&nbsp;876&nbsp;797,53</td><td style="text-align:right;">43&nbsp;443&nbsp;195&nbsp;035,04</td><td style="text-align:right;">12&nbsp;612&nbsp;648&nbsp;838,00</td><td style="text-align:right;">11&nbsp;995&nbsp;411&nbsp;291,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">12&nbsp;172&nbsp;802&nbsp;862,67</td><td style="text-align:right;">39&nbsp;768&nbsp;342&nbsp;676,62</td><td style="text-align:right;">11&nbsp;510&nbsp;111&nbsp;399,00</td><td style="text-align:right;">12&nbsp;134&nbsp;877&nbsp;571,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">13&nbsp;634&nbsp;041&nbsp;965,14</td><td style="text-align:right;">48&nbsp;209&nbsp;231&nbsp;343,05</td><td style="text-align:right;">12&nbsp;608&nbsp;691&nbsp;718,00</td><td style="text-align:right;">12&nbsp;815&nbsp;242&nbsp;585,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">13&nbsp;104&nbsp;596&nbsp;804,38</td><td style="text-align:right;">44&nbsp;113&nbsp;167&nbsp;148,17</td><td style="text-align:right;">12&nbsp;626&nbsp;278&nbsp;785,00</td><td style="text-align:right;">13&nbsp;205&nbsp;353&nbsp;501,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">12&nbsp;754&nbsp;659&nbsp;043,69</td><td style="text-align:right;">41&nbsp;543&nbsp;644&nbsp;059,26</td><td style="text-align:right;">11&nbsp;613&nbsp;585&nbsp;485,00</td><td style="text-align:right;">11&nbsp;452&nbsp;923&nbsp;855,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">13&nbsp;514&nbsp;101&nbsp;879,06</td><td style="text-align:right;">40&nbsp;886&nbsp;554&nbsp;950,92</td><td style="text-align:right;">12&nbsp;978&nbsp;091&nbsp;752,00</td><td style="text-align:right;">12&nbsp;789&nbsp;548&nbsp;820,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">11&nbsp;465&nbsp;779&nbsp;764,41</td><td style="text-align:right;">40&nbsp;908&nbsp;711&nbsp;754,63</td><td style="text-align:right;">10&nbsp;081&nbsp;863&nbsp;504,00</td><td style="text-align:right;">9&nbsp;777&nbsp;959&nbsp;395,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">12&nbsp;726&nbsp;037&nbsp;506,73</td><td style="text-align:right;">41&nbsp;703&nbsp;962&nbsp;147,89</td><td style="text-align:right;">12&nbsp;399&nbsp;248&nbsp;090,00</td><td style="text-align:right;">12&nbsp;392&nbsp;071&nbsp;524,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">12&nbsp;588&nbsp;359&nbsp;370,70</td><td style="text-align:right;">41&nbsp;130&nbsp;727&nbsp;933,85</td><td style="text-align:right;">11&nbsp;558&nbsp;601&nbsp;330,00</td><td style="text-align:right;">12&nbsp;517&nbsp;106&nbsp;390,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">12&nbsp;121&nbsp;740&nbsp;572,30</td><td style="text-align:right;">43&nbsp;492&nbsp;324&nbsp;675,64</td><td style="text-align:right;">11&nbsp;108&nbsp;916&nbsp;259,00</td><td style="text-align:right;">11&nbsp;725&nbsp;231&nbsp;343,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">11&nbsp;122&nbsp;182&nbsp;554,30</td><td style="text-align:right;">41&nbsp;572&nbsp;222&nbsp;679,35</td><td style="text-align:right;">11&nbsp;519&nbsp;468&nbsp;515,00</td><td style="text-align:right;">12&nbsp;396&nbsp;999&nbsp;154,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">11&nbsp;917&nbsp;112&nbsp;381,72</td><td style="text-align:right;">42&nbsp;889&nbsp;680&nbsp;221,37</td><td style="text-align:right;">12&nbsp;077&nbsp;298&nbsp;548,00</td><td style="text-align:right;">13&nbsp;890&nbsp;623&nbsp;811,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:29:23 WIB</em></caption></table>'
html_2014 = '<table id="summaryexim" class="table table-sm table-striped table-bordered thead-light "><thead><tr><td align="center">No.</td><td align="center">Bulan</td><td align="center">Nilai Ekspor (US $)</td><td align="center">Berat Ekspor (KG)</td><td align="center">Nilai Impor (US $)</td><td align="center">Berat Impor (KG)</td></tr></thead><tbody><tr><td>1</td><td>Januari</td><td style="text-align:right;">14&nbsp;472&nbsp;289&nbsp;332,00</td><td style="text-align:right;">49&nbsp;154&nbsp;384&nbsp;703,00</td><td style="text-align:right;">14&nbsp;916&nbsp;227&nbsp;693,00</td><td style="text-align:right;">11&nbsp;590&nbsp;996&nbsp;964,00</td></tr><tr><td>2</td><td>Februari</td><td style="text-align:right;">14&nbsp;634&nbsp;090&nbsp;390,00</td><td style="text-align:right;">43&nbsp;416&nbsp;241&nbsp;019,00</td><td style="text-align:right;">13&nbsp;790&nbsp;661&nbsp;990,00</td><td style="text-align:right;">10&nbsp;640&nbsp;029&nbsp;636,00</td></tr><tr><td>3</td><td>Maret</td><td style="text-align:right;">15&nbsp;192&nbsp;634&nbsp;701,00</td><td style="text-align:right;">49&nbsp;294&nbsp;958&nbsp;689,00</td><td style="text-align:right;">14&nbsp;523&nbsp;719&nbsp;412,00</td><td style="text-align:right;">11&nbsp;439&nbsp;923&nbsp;450,00</td></tr><tr><td>4</td><td>April</td><td style="text-align:right;">14&nbsp;292&nbsp;472&nbsp;554,00</td><td style="text-align:right;">45&nbsp;541&nbsp;731&nbsp;344,00</td><td style="text-align:right;">16&nbsp;254&nbsp;976&nbsp;317,00</td><td style="text-align:right;">13&nbsp;005&nbsp;419&nbsp;405,00</td></tr><tr><td>5</td><td>Mei</td><td style="text-align:right;">14&nbsp;823&nbsp;602&nbsp;661,00</td><td style="text-align:right;">47&nbsp;417&nbsp;633&nbsp;575,00</td><td style="text-align:right;">14&nbsp;770&nbsp;336&nbsp;777,00</td><td style="text-align:right;">12&nbsp;197&nbsp;088&nbsp;101,00</td></tr><tr><td>6</td><td>Juni</td><td style="text-align:right;">15&nbsp;409&nbsp;451&nbsp;765,00</td><td style="text-align:right;">44&nbsp;989&nbsp;016&nbsp;798,00</td><td style="text-align:right;">15&nbsp;697&nbsp;742&nbsp;441,00</td><td style="text-align:right;">12&nbsp;811&nbsp;352&nbsp;690,00</td></tr><tr><td>7</td><td>Juli</td><td style="text-align:right;">14&nbsp;124&nbsp;129&nbsp;298,00</td><td style="text-align:right;">43&nbsp;624&nbsp;537&nbsp;982,00</td><td style="text-align:right;">14&nbsp;081&nbsp;710&nbsp;235,00</td><td style="text-align:right;">11&nbsp;541&nbsp;376&nbsp;167,00</td></tr><tr><td>8</td><td>Agustus</td><td style="text-align:right;">14&nbsp;481&nbsp;642&nbsp;319,00</td><td style="text-align:right;">43&nbsp;484&nbsp;947&nbsp;226,00</td><td style="text-align:right;">14&nbsp;793&nbsp;236&nbsp;965,00</td><td style="text-align:right;">11&nbsp;676&nbsp;185&nbsp;855,00</td></tr><tr><td>9</td><td>September</td><td style="text-align:right;">15&nbsp;275&nbsp;846&nbsp;089,00</td><td style="text-align:right;">46&nbsp;043&nbsp;270&nbsp;707,00</td><td style="text-align:right;">15&nbsp;546&nbsp;096&nbsp;309,00</td><td style="text-align:right;">13&nbsp;158&nbsp;825&nbsp;424,00</td></tr><tr><td>10</td><td>Oktober</td><td style="text-align:right;">15&nbsp;292&nbsp;759&nbsp;010,00</td><td style="text-align:right;">43&nbsp;705&nbsp;129&nbsp;574,00</td><td style="text-align:right;">15&nbsp;327&nbsp;994&nbsp;527,00</td><td style="text-align:right;">13&nbsp;184&nbsp;342&nbsp;220,00</td></tr><tr><td>11</td><td>November</td><td style="text-align:right;">13&nbsp;544&nbsp;729&nbsp;209,00</td><td style="text-align:right;">46&nbsp;182&nbsp;204&nbsp;245,00</td><td style="text-align:right;">14&nbsp;041&nbsp;608&nbsp;394,00</td><td style="text-align:right;">12&nbsp;258&nbsp;277&nbsp;415,00</td></tr><tr><td>12</td><td>Desember</td><td style="text-align:right;">14&nbsp;436&nbsp;339&nbsp;660,00</td><td style="text-align:right;">46&nbsp;611&nbsp;395&nbsp;610,00</td><td style="text-align:right;">14&nbsp;434&nbsp;652&nbsp;028,00</td><td style="text-align:right;">14&nbsp;230&nbsp;519&nbsp;275,00</td></tr></tbody><caption><em>Sumber : https://www.bps.go.id diakses pada 09-06-2023 16:29:36 WIB</em></caption></table>'

def scrape_table(table_tag, year):
    # Get the <table> HTML tag
    html = table_tag

    # Read the HTML table
    df = pd.read_html(html)[0]
    df.reset_index(drop=True, inplace=True)
    df['Tahun'] = year
    return df

def convert_to_numerical(df):
    df['Nilai Ekspor (US $)'] = df['Nilai Ekspor (US $)'].str.replace('\xa0', '').str.replace(',', '.').astype(float)
    df['Berat Ekspor (KG)'] = df['Berat Ekspor (KG)'].str.replace('\xa0', '').str.replace(',', '.').astype(float)
    df['Nilai Impor (US $)'] = df['Nilai Impor (US $)'].str.replace('\xa0', '').str.replace(',', '.').astype(float)
    df['Berat Impor (KG)'] = df['Berat Impor (KG)'].str.replace('\xa0', '').str.replace(',', '.').astype(float)

    return df

def set_page_configuration():
    st.set_page_config(page_title = 'Tetris 3 Capstone Project',
                       page_icon = '📊',
                       layout = 'wide',
                       initial_sidebar_state = 'expanded')

def introduction(df):
    st.title('Analisis Perkembangan Ekspor-Impor Indonesia 10 Tahun Terakhir')
    st.write('Presiden Joko Widodo menegaskan bahwa pemerintah akan terus mendorong program **hilirisasi industri** dengan mengurangi ekspor bahan mentah (*raw material*) untuk **meningkatkan nilai tambah** di sektor industri dan membuka lapangan kerja bagi rakyat Indonesia. Menurut Presiden, sebuah negara dapat dikatakan sebagai negara maju jika negara-negara lain telah memiliki ketergantungan terhadap suatu produk yang dihasilkan oleh negara maju tersebut. Dengan melakukan hilirisasi, negara dapat meningkatkan kemampuan produksi sumber daya alam menjadi barang jadi atau setengah jadi agar bisa bersaing di tingkat global.')

    with st.expander('Sumber Data'):
        st.info('Badan Pusat Statistik - Data Ekspor Impor Tahun 2014 - 2023 (https://www.bps.go.id/exim/)')

    displayed_df = df.copy()
    displayed_df['Tahun'] = displayed_df['Tahun'].astype('str')

    with st.expander('Lihat Data Tabular'):
        sort_type = st.selectbox(label = 'Sortir Tahun', options = ['Terbaru', 'Terlama'])
        ascending = True if sort_type == 'Terlama' else False
        st.dataframe(displayed_df.sort_values('Tahun', ascending = ascending).reset_index().drop('index', axis = 1), use_container_width = True)

def plot_line_chart(pivot_df, value_or_weight, export_or_import):
    # Plotly Chart
    unit = '(US $)' if value_or_weight == 'Nilai' else '(KG)'
    fig = px.line(pivot_df, x = 'Tahun', y = f'{value_or_weight} {export_or_import} {unit}')
    fig.update_layout(title = f'Perkembangan {value_or_weight} {export_or_import} Indonesia',
                      yaxis_title = f'{value_or_weight} {export_or_import} {unit}')

    return fig

def display_metric(pivot_df, previous_year, current_year, value_or_weight, export_or_import):
    unit = '(US $)' if value_or_weight == 'Nilai' else '(KG)'
    previous = float(pivot_df.loc[pivot_df['Tahun'] == previous_year, f'{value_or_weight} {export_or_import} {unit}'])
    current = float(pivot_df.loc[pivot_df['Tahun'] == current_year, f'{value_or_weight} {export_or_import} {unit}'])
    diff = current - previous
    diff_percentage = diff * 100 / previous
    unit_info = f'USD {round(diff, 2)}' if value_or_weight == 'Nilai' else f'{round(diff, 2)} kg'
    st.metric(f'Perubahan {value_or_weight} {export_or_import}', unit_info, f'{round(diff_percentage, 2)}%')

def plot_export_import_correlation(df, value_or_weight, selected_years):
    unit = '(US $)' if value_or_weight == 'Nilai' else '(KG)'

    # Filter the DataFrame based on the selected years
    if 'Semua Tahun' in selected_years:
        data = df.copy()
        selected_years = df['Tahun'].unique()
    else:
        data = df[df['Tahun'].isin(selected_years)]

    # Create a scatter plot for the selected years
    fig = go.Figure()
    for year in selected_years:
        scatter = go.Scatter(x=data[data['Tahun'] == year][f'{value_or_weight} Ekspor {unit}'],
                             y=data[data['Tahun'] == year][f'{value_or_weight} Impor {unit}'],
                             mode='markers', name=str(year))
        fig.add_trace(scatter)

    # Set plot layout
    fig.update_layout(title=f'Hubungan {value_or_weight} Ekspor dan {value_or_weight} Impor',
                      xaxis_title=f'{value_or_weight} Ekspor',
                      yaxis_title=f'{value_or_weight} Impor',
                      hovermode='closest')

    # Display the plot
    return fig

def plot_top_countries_by_export_value():
    st.markdown(f'<h3 style="text-align: center">Statistik Nilai Ekspor Tertinggi ke Negara Tujuan</h3>', unsafe_allow_html = True)

    export_by_country_df = pd.read_csv('Perkembangan Ekspor Non Migas (Negara Tujuan).csv').head(5)
    countries = export_by_country_df['Negara']
    years = export_by_country_df.columns[1:]  # Exclude the 'Negara' column

    # Colors for the countries
    color_dict = {
        'China': '#ba1206',
        'United States': '#1203ad',
        'India': '#00a613',
        'Japan': '#ffffff',
        'Malaysia': '#f7db05',
        'Philippines': '#1500ff',
        'South Korea': '#006eff',
        'Singapore': '#ff1100',
        'Vietnam': '#d61204',
        'Taiwan': '#fa795f',
        'Thailand': '#0e2aaa',
        'Netherlands': '#808080',
        'Pakistan': '#808080',
        'Bangladesh': '#808080',
        'Australia': '#808080'
    }

    # Create a line plot figure with custom colors
    fig = go.Figure()

    for country in countries:
        country_data = export_by_country_df.loc[export_by_country_df['Negara'] == country, years]
        fig.add_trace(go.Line(
            x=years,
            y=country_data.values.flatten(),
            name=country,
            marker=dict(color=color_dict.get(country, '#808080'))
        ))

    # Set chart title and axis labels
    fig.update_layout(
        title='Nilai Ekspor Tertinggi ke Negara Tujuan Tahun 2022',
        xaxis_title='Year',
        yaxis_title='Nilai Ekspor (juta USD)'
    )

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.write('Dari grafik batang di atas, dapat dilihat bahwa Republik Rakyat Tiongkok adalah konsumen non-migas terbesar, diikuti oleh Amerika Serikat, India, Jepang, dan Malaysia. Tiongkok juga mengalami kenaikan nilai impor signifikan pada rentang tahun 2020 hingga 2022. Negara-negara lainnya di 5 besar mengalami kenaikan namun tidak sepesat Tiongkok.')

    with st.expander('Lihat Lebih Detail Statistik per Tahun'):
        export_by_country_df = pd.read_csv('Perkembangan Ekspor Non Migas (Negara Tujuan).csv')
        st.markdown('<hr>', unsafe_allow_html=True)
        year = st.slider(label = 'Tahun', min_value = 2018, max_value = 2022, value = 2022)
        export_by_country_df[str(year)] = export_by_country_df[str(year)].str.replace(',', '').astype(float)
        top_10_countries = export_by_country_df.nlargest(10, str(year))
        top_10_countries = top_10_countries.sort_values(str(year), ascending=False)

        # Extract the required data for the chart
        countries = top_10_countries['Negara']
        values = top_10_countries[str(year)]

        # Define custom colors for the countries
        color_dict = {
            'China': '#ba1206',
            'United States': '#001160',
            'India': '#00a613',
            'Japan': '#ffffff',
            'Malaysia': '#f7db05',
            'Philippines': '#1500ff',
            'South Korea': '#006eff',
            'Singapore': '#ff1100',
            'Vietnam': '#d61204',
            'Taiwan': '#fa795f',
            'Thailand': '#0e2aaa'
        }

        # Create a horizontal bar chart figure with custom colors
        fig = go.Figure(data=go.Bar(
            y=countries,
            x=values,
            text=[str(round(v / 1000, 1)) + 'k' for v in values],
            textposition='auto',
            orientation='h'
        ))

        # Set custom colors for each bar using color_dict
        colors = [color_dict.get(country, '#808080') for country in countries]
        fig.update_traces(marker=dict(color=colors))

        # Set chart title and axis labels
        fig.update_layout(
            title = f'10 Negara Tujuan Teratas Ekspor Non-Migas Tahun {year}',
            xaxis_title = 'Nilai Ekspor Non-Migas (juta USD)',
            yaxis_title = 'Negara'
        )

        fig.update_yaxes(autorange = 'reversed')
        st.plotly_chart(fig, use_container_width=True)
        st.write('Angka nilai ekspor pada negara-negara dengan 10 nilai ekspor tertinggi cenderung menunjukkan peningkatan moderat. Peningkatan paling signifikan adalah Tiongkok dengan peningkatan nilai ekspor sebesar 62% pada 5 tahun terakhir.')

def plot_nickel_producer():
    df = pd.read_csv('Produsen Nikel.csv')

    fig = go.Figure(data=go.Bar(
        x=df['Produksi Nikel (ribu ton)'],
        y=df['Negara'],
        text=df['Produksi Nikel (ribu ton)'],
        textposition='auto',
        orientation='h',
        marker_color='green'  # Set the color of the bars
    ))

    fig.update_layout(
        title='Produksi Nikel per Negara',
        xaxis_title='Produksi Nikel (ribu ton)',
        yaxis_title='Negara'
    )

    fig.update_yaxes(autorange = 'reversed')
    st.plotly_chart(fig, use_container_width=True)

def plot_export_by_commodity():
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: center">Statistik Komoditas Ekspor Tertinggi</h3>', unsafe_allow_html = True)
    export_by_commodity_df = pd.read_csv('Perkembangan Ekspor Non Migas (Komoditi).csv')
    year = st.slider(label='Tahun', min_value=2018, max_value=2022, value=2022, key='export_year_slider')
    export_by_commodity_df[str(year)] = export_by_commodity_df[str(year)].str.replace(',', '').astype(float)
    top_10_commodities = export_by_commodity_df.nlargest(15, str(year))
    top_10_commodities = top_10_commodities.sort_values(str(year), ascending=False)

    commodities = top_10_commodities['Komoditas']
    values = top_10_commodities[str(year)]

    fig = go.Figure(data=go.Bar(
        x=values,
        y=commodities,
        text=[str(round(v / 1000, 1)) + 'k' for v in values],
        textposition='auto',
        orientation='h',
        marker=dict(
            color='green',
            line=dict(color='rgba(58, 71, 80, 1)', width=1)
        )
    ))

    fig.update_layout(
        title=f'10 Komoditas Ekspor Non-Migas Teratas Tahun {year}',
        xaxis_title='Nilai Ekspor Non-Migas (juta USD)',
        yaxis_title='Komoditas',
        showlegend=False,
        height=750
    )

    fig.update_yaxes(autorange='reversed')

    # Display the chart in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    st.write('Komoditas nikel yang menjadi salah satu prioritas utama pemerintah masih belum masuk ke dalam 10 besar komoditas dengan nilai ekspor tertinggi. Nilai ekspor nikel baru mengalami peningkatan dan masuk ke 15 besar pada tahun 2022. Pemerintah dapat terus menarik perusahaan atau pabrik mancanegara untuk mengolah sumber daya mentah menjadi barang jadi untuk meningkatkan nilai ekspor.')

def display_home():
    data = [scrape_table(html_2023, 2023).sort_values('No.', ascending = False),
            scrape_table(html_2022, 2022).sort_values('No.', ascending = False),
            scrape_table(html_2021, 2021).sort_values('No.', ascending = False),
            scrape_table(html_2020, 2020).sort_values('No.', ascending = False),
            scrape_table(html_2019, 2019).sort_values('No.', ascending = False),
            scrape_table(html_2018, 2018).sort_values('No.', ascending = False),
            scrape_table(html_2017, 2017).sort_values('No.', ascending = False),
            scrape_table(html_2016, 2016).sort_values('No.', ascending = False),
            scrape_table(html_2015, 2015).sort_values('No.', ascending = False),
            scrape_table(html_2014, 2014).sort_values('No.', ascending = False)]

    df = pd.concat(data)
    df = df[~(df['Nilai Ekspor (US $)'] == 'belum rilis')]
    convert_to_numerical(df)

    introduction(df.drop('No.', axis = 1))

    agg_function = 'mean'
    pivot_df = pd.pivot_table(data = df,
                              index = 'Tahun',
                              aggfunc = {'Nilai Ekspor (US $)': agg_function,
                                         'Nilai Impor (US $)': agg_function,
                                         'Berat Ekspor (KG)': agg_function,
                                         'Berat Impor (KG)': agg_function}).reset_index()

    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: center"> Grafik Nilai dan Berat Ekspor/Impor </h3>', unsafe_allow_html = True)

    # LINE CHART (Export/Import Value and Weight)
    figures = []
    figures.append(plot_line_chart(pivot_df, 'Nilai', 'Ekspor'))
    figures.append(plot_line_chart(pivot_df, 'Nilai', 'Impor'))
    figures.append(plot_line_chart(pivot_df, 'Berat', 'Ekspor'))
    figures.append(plot_line_chart(pivot_df, 'Berat', 'Impor'))

    col1, col2 = st.columns(2)
    st.plotly_chart(figures[0])
    st.plotly_chart(figures[1])

    export_import_df = pivot_df[['Tahun', 'Nilai Ekspor (US $)', 'Nilai Impor (US $)']]
    styled_df = export_import_df.copy()
    styled_df['Surplus / Defisit'] = styled_df['Nilai Ekspor (US $)']

    # Highlight whether it is a surplus or defisit
    mask = styled_df['Nilai Ekspor (US $)'] > styled_df['Nilai Impor (US $)']
    styled_df.loc[mask, 'Surplus / Defisit'] = 'Surplus'
    styled_df.loc[~mask, 'Surplus / Defisit'] = 'Defisit'

    # Display the styled DataFrame with actual color
    st.write(styled_df.style.apply(lambda x: x.map({'Surplus': 'background-color: green',
                                                    'Defisit': 'background-color: red'})),
             unsafe_allow_html = True)

    st.write('Lemahnya ekspor Indonesia di tahun 2016 dikarenakan oleh melemahnya beberapa harga komoditas, seperti kopi, lada hitam, putih, kakao, rumput laut, dan tanaman obat. Permintaan global yang tak kunjung naik juga membuat volume ekspor Indonesia masih belum bisa bangkit, menurut Kepala BPS Suhariyanto.')
    # (https://www.cnnindonesia.com/ekonomi/20170116121413-92-186589/2016-ekspor-indonesia-turun-jadi-us-14443-miliar)

    st.write('Sedangkan defisit pada tahun 2018 merupakan yang terparah dalam 10 tahun terakhir karena kenaikan harga minyak sehingga berdampak langsung pada nilai ekspor bahan migas.')
    # (https://www.cnbcindonesia.com/news/20190115125640-4-50740/waduh-defisit-dagang-ri-2018-terparah-sepanjang-sejarah)'

    with st.expander('Lihat juga Perkembangan Berat Ekspor-Impor'):
        st.plotly_chart(figures[2])
        st.plotly_chart(figures[3])

    # METRICS
    st.markdown('<hr>', unsafe_allow_html=True)
    st.write('Tinjau perkembangan ekspor / impor dalam rentang tahun tertentu dengan mengatur interval berikut:')
    previous_year, current_year = st.slider(label = 'Rentang Tahun', min_value = 2014, max_value = 2023, value = [2014, 2023])

    export_import_stats_markdown = f'Statistik Ekspor dan Impor Tahun ({previous_year} - {current_year})'
    st.markdown(f'<h3 style="text-align: center"> {export_import_stats_markdown} </h3>', unsafe_allow_html = True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_metric(pivot_df, previous_year, current_year, 'Nilai', 'Ekspor')
    with col2:
        display_metric(pivot_df, previous_year, current_year, 'Nilai', 'Impor')
    with col3:
        display_metric(pivot_df, previous_year, current_year, 'Berat', 'Ekspor')
    with col4:
        display_metric(pivot_df, previous_year, current_year, 'Berat', 'Impor')

    # CORRELATION ANALYSIS
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown(f'<h3 style="text-align: center"> Analisis Korelasi Nilai dan Berat Ekspor/Impor </h3>', unsafe_allow_html = True)
    col1, col2 = st.columns(2)
    with col1:
        st.image('Nilai Ekspor vs Nilai Impor.gif', width = 500)
        st.caption('Hubungan Nilai Ekspor dan Impor')
    with col2:
        st.image('Berat Ekspor vs Berat Impor.gif', width = 500)
        st.caption('<p style="text-align:center padding-left:200px;">Hubungan Berat Ekspor dan Impor</p>', unsafe_allow_html=True)

    selected_years = st.multiselect('Tampilkan Data Berdasarkan Tahun', ['Semua Tahun'] + list(df['Tahun'].unique()), default = 'Semua Tahun')
    figures = []
    figures.append(plot_export_import_correlation(df, 'Nilai', selected_years))
    figures.append(plot_export_import_correlation(df, 'Berat', selected_years))

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(figures[0])
    with col2:
        st.plotly_chart(figures[1])

    with st.expander('Analisis Korelasi'):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h4 style=\"color:#FFFFFF\">Nilai Ekspor dan Impor</h4>", unsafe_allow_html=True)
            st.markdown(f"<h3 style=\"color:#32C9FF\">{round(df[['Nilai Ekspor (US $)', 'Nilai Impor (US $)']].corr(method='spearman').iloc[0][1] * 100, 2)}%</h3>", unsafe_allow_html=True)
        with col2:
            st.markdown("<h4 style=\"color:#FFFFFF\">Berat Ekspor dan Impor</h4>", unsafe_allow_html=True)
            st.markdown(f"<h3 style=\"color:#32C9FF\">{round(df[['Berat Ekspor (KG)', 'Berat Impor (KG)']].corr(method='spearman').iloc[0][1] * 100, 2)}%</h3>", unsafe_allow_html=True)

        st.markdown('<hr>', unsafe_allow_html=True)
        st.write('Grafik dan angka korelasi di atas menunjukkan bahwa nilai dan berat ekspor-impor cukup berkaitan satu sama lain. Nilai ekspor dan nilai impor memiliki hubungan positif yang sangat kuat yang berarti jika nilai ekspor meningkat, nilai impor juga cenderung meningkat. Berat ekspor dan berat impor adalah moderat, yang menunjukkan adanya hubungan berbanding lurus (positif) namun tidak sekuat hubungan nilai ekspor dan impor.')

    # st.markdown('<hr>', unsafe_allow_html=True)
    # year = st.slider(label = 'Tahun', min_value = 2018, max_value = 2022, value = 2022)
    st.markdown('<hr>', unsafe_allow_html=True)
    plot_top_countries_by_export_value()


def display_world_export_map(year):
    # Use the iframe HTML tag to embed the Tableau visualization
    embed_code_2022 = """
    <div class='tableauPlaceholder' id='viz1686545074181' style='position: relative'><noscript><a href='#'><img alt='Peta Ekspor Non-Migas Tahun 2022 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaEksporNon-Migas2022&#47;2022&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PetaEksporNon-Migas2022&#47;2022' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaEksporNon-Migas2022&#47;2022&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686545074181');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    embed_code_2021 = """
    <div class='tableauPlaceholder' id='viz1686561055788' style='position: relative'><noscript><a href='#'><img alt='2021 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;MM&#47;MMTRZBK32&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;MMTRZBK32' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;MM&#47;MMTRZBK32&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686561055788');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    embed_code_2020 = """
    <div class='tableauPlaceholder' id='viz1686574369317' style='position: relative'><noscript><a href='#'><img alt='2020 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;3R&#47;3RMT2HNBZ&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;3RMT2HNBZ' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;3R&#47;3RMT2HNBZ&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686574369317');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    embed_code_2019 = """
    <div class='tableauPlaceholder' id='viz1686574581361' style='position: relative'><noscript><a href='#'><img alt='2019 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaEksporNon-Migas2022&#47;2019&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PetaEksporNon-Migas2022&#47;2019' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaEksporNon-Migas2022&#47;2019&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686574581361');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """
    embed_code_2018 = """
    <div class='tableauPlaceholder' id='viz1686574697435' style='position: relative'><noscript><a href='#'><img alt='2018 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaEksporNon-Migas2022&#47;2018&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PetaEksporNon-Migas2022&#47;2018' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Pe&#47;PetaEksporNon-Migas2022&#47;2018&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1686574697435');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
    """

    if year == 2022:
        embed_code = embed_code_2022
    elif year == 2021:
        embed_code = embed_code_2021
    elif year == 2020:
        embed_code = embed_code_2020
    elif year == 2019:
        embed_code = embed_code_2019
    elif year == 2018:
        embed_code = embed_code_2018

    st.components.v1.html(embed_code, height = 600)

def main():
    set_page_configuration()
    menu_selection = st.sidebar.selectbox('Pilih Halaman', ('🏠┆Beranda', '🗺️┆Peta Nilai Ekspor Dunia'))
    st.sidebar.caption('Tutup sidebar ini untuk menampilkan visualisasi dengan layar penuh.')
    if menu_selection == '🏠┆Beranda':
        display_home()
        plot_export_by_commodity()
        plot_nickel_producer()
    elif menu_selection == '🗺️┆Peta Nilai Ekspor Dunia':
        st.header('Peta Nilai Ekspor Dunia')
        st.write('Ingin mengkaji nilai ekspor ke negara secara lebih spesifik? Lihat peta berikut dan atur tahunnya.')
        year = st.slider(label = 'Tahun', min_value = 2018, max_value = 2022, value = 2022)
        display_world_export_map(year)
        st.write('Peta ekspor dunia di atas menunjukkan secara lengkap seberapa besar nilai ekspor Indonesia ke negara lain di seleuruh dunia, yang memungkinkan untuk melihat nilai ekspor negara yang berada di luar 10 teratas. Pemerintah Indonesia juga dapat meningkatkan nilai ekspor ke negara-negara tersebut guna meningkatkan nilai ekspor sumber daya alam yang dimiliki Indonesia pada masa yang akan datang.')

if __name__ == '__main__':
    main()
