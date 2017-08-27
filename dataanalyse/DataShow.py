#  显示北京住房数据的正太分布图
import pandas as pd
import matplotlib.pyplot as plot
import json


def line_json_load(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        df = pd.DataFrame()
        i = 0
        for line in lines:
            tmp_df = pd.DataFrame(json.loads(line), index=[i])
            tmp_df["price"] = tmp_df["price"].astype("int")
            tmp_df["area"] = tmp_df["area"].astype("float")
            tmp_df["lng"] = tmp_df["lng"].astype("float")
            tmp_df["lat"] = tmp_df["lat"].astype("float")
            if tmp_df.iloc[0]["time_unit"] == "每天":
                tmp_df.price[i] = tmp_df.price[i] * 30

            df = df.append(tmp_df)
            i += 1
            print(i)
        return df


filename = 'F:\\Github\\Python\\dataanalyse\\ziroomBeijing.json'
df = line_json_load(filename)
df = df.drop_duplicates()
df = df[(df['time_unit'] != '每天') & (df['direction'] != '南北') & (df['floorLoc'] != '') & (df['floorTotal'] != '')]

# 不同租赁方式的统计量
# df["price_per_m2"] = df["price"]/df["area"]
groups = df.groupby(df["rentType"])
rt_count = groups.size()
rt_mean = groups.mean().rename(columns={'price': 'mean_price'})
rt_max = groups.max().rename(columns={'price': 'max_price'})
rt_min = groups.min().rename(columns={'price': 'min_price'})
rt_median = groups.median().rename(columns={'price': 'median_price'})
rentTypeDf = pd.concat(
    [rt_mean["mean_price"], pd.DataFrame(rt_count, columns=["count"]), rt_max["max_price"], rt_min["min_price"],
     rt_median["median_price"]], axis=1)

# df[df['price']==990]["link"]
############合租分析############
# 每100元为区间段统计数量
he_intervals = {100 * x: 0 for x in range(64)}
for price in df[df['rentType'] == '合']['price']:
    he_intervals[price // 100 * 100] += 1
plot.bar(list(he_intervals.keys()), list(he_intervals.values()), width=100, alpha=0.5, color='blue')
plot.xlabel(u"月租(元)", fontproperties='SimHei')
plot.ylabel(u"房间数量", fontproperties='SimHei')
plot.show()
