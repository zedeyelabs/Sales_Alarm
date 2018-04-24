{
  "paragraphs": [
    {
      "title": "Import Functions",
      "text": "%pyspark\n\nfrom pyspark.sql import *\nfrom pyspark.sql.functions import col, when, max, min\nfrom pyspark.sql.functions import count, sum,avg\nfrom pyspark.sql.functions import desc\nfrom pyspark.sql.functions import col, round\nfrom datetime import datetime, timedelta as td\nfrom pyspark.sql.functions import datediff,to_date,to_timestamp\nfrom pyspark.sql.functions import countDistinct\nfrom pyspark.sql.functions import lit\nfrom pyspark.sql.functions import substring\nfrom pyspark.sql.functions import broadcast\nspark.version",
      "user": "info@zedeyelabs.com",
      "dateUpdated": "Apr 24, 2018 12:46:53 PM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523181296642_1073568728",
      "id": "20180408-095456_1483174345_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "u\u00272.2.0\u0027\n"
      },
      "dateCreated": "Apr 8, 2018 9:54:56 AM",
      "dateStarted": "Apr 24, 2018 12:46:53 PM",
      "dateFinished": "Apr 24, 2018 12:46:53 PM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "text": "%pyspark\n\nprint \"Hello\"",
      "user": "info@zedeyelabs.com",
      "dateUpdated": "Apr 24, 2018 12:48:54 PM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python"
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1524574123085_1495766742",
      "id": "20180424-124843_163139589_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "Hello\n"
      },
      "dateCreated": "Apr 24, 2018 12:48:43 PM",
      "dateStarted": "Apr 24, 2018 12:48:54 PM",
      "dateFinished": "Apr 24, 2018 12:48:54 PM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Date Definition",
      "text": "%pyspark\n\ntoday \u003d (datetime.today() - td(days\u003d0))\n\nd0 \u003d (today - td(days\u003d1)).date()\nd1 \u003d (today - td(days\u003d2)).date()\nd6 \u003d (today - td(days\u003d6)).date()\nd7 \u003d (today - td(days\u003d8)).date()\nd14 \u003d (today - td(days\u003d15)).date()\nd21 \u003d (today - td(days\u003d22)).date()\nd28 \u003d (today - td(days\u003d29)).date()\nd180 \u003d (today - td(days\u003d180)).date()\n\nprint d0,d1,d6,d7,d14,d21,d28,d180",
      "user": "info@zedeyelabs.com",
      "dateUpdated": "Apr 24, 2018 11:14:06 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523264800524_743527585",
      "id": "20180409-090640_903259713_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "2018-04-23 2018-04-22 2018-04-18 2018-04-16 2018-04-09 2018-04-02 2018-03-26 2017-10-26\n"
      },
      "dateCreated": "Apr 9, 2018 9:06:40 AM",
      "dateStarted": "Apr 24, 2018 11:14:06 AM",
      "dateFinished": "Apr 24, 2018 11:14:06 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Sales Calculations",
      "text": "%pyspark\n\n################### Source Data ######################\n\n\nlot_stk_move \u003d spark.sql(\"select * from dub_gcity.zed_lot_stk_move\")\\\n                        .fillna({\u0027tsm_qty_pack\u0027:\u00270\u0027,\u0027tsm_qty_loose\u0027:\u00270\u0027,\u0027tsm_conv_lsstk\u0027:\u00271\u0027})\\\n                        .withColumn(\"tsm_qty_total\",col(\"tsm_qty_pack\")+col(\"tsm_qty_loose\")/col(\"tsm_conv_lsstk\"))\\\n                        .withColumn(\"tsm_cre_date\",to_date(\"tsm_cre_dt\"))\\\n                        .filter(col(\"tsm_cre_date\")\u003e\u003dd180)\\\n                        .filter(col(\"tsm_cre_date\")\u003ctoday.date())\n\nlot_trn_head \u003d spark.sql(\"select * from dub_gcity.zed_lot_trn_head\").withColumn(\"trxh_cre_date\",to_date(\"trxh_cre_dt\")).filter(col(\"trxh_cre_date\")\u003e\u003dd28)\nbroadcast(lot_trn_head)\n\nlot_stk_move1 \u003d lot_stk_move.join(lot_trn_head,col(\"tsm_doc_no\")\u003d\u003dcol(\"trxh_doc_no\"),\"inner\")\nlot_stk_move1.cache()\n\nProducts \u003d spark.sql(\"select prod_code as tsm_prod_code,prod_desc as Prod_Description,prod_div_code from dub_ho.zed_lom_mst_product\")\n\nMaster \u003d spark.sql(\"select camd_entity_code as prod_div_code,camd_entity_desc as Prod_Division from dub_ho.zed_lom_mst_carry_all_detl where camd_entity_group\u003d\u0027DIVISION\u0027\")\n\n################## Data Check #############################\nif(lot_stk_move1.filter(col(\"tsm_cre_dt\")\u003e\u003dto_timestamp(lit((str(d0)+\" 21:00:00\")), \"yyyy-MM-dd HH:mm:ss\")).count()\u003d\u003d0):\n    print(\"No data present for yesterday\")\n    exit()\nelse:\n    print(\"Data present for yesterday\")\n################## Product Classification #################\n\nProduct_Class \u003d lot_stk_move.groupBy(\"tsm_prod_code\")\\\n                .agg(min(\"tsm_cre_date\").alias(\"Min_Date\"),sum(\"tsm_lc_value\").alias(\"Total_Sales\"),countDistinct(\"tsm_cre_date\").alias(\"Days_Sold\"))\\\n                .withColumn(\"Total_Days\",datediff(lit(today.date()),col(\"Min_Date\")))\\\n                .withColumn(\"Days_Sold_Ratio\",col(\"Days_Sold\")/col(\"Total_Days\"))\\\n                .withColumn(\"Cum_Sales\",sum(\"Total_Sales\").over(Window.partitionBy().orderBy(desc(\"Total_Sales\"))))\\\n                .withColumn(\"Store_Sales\",sum(\"Total_Sales\").over(Window.partitionBy()))\\\n                .withColumn(\"Perc\",col(\"Cum_Sales\")/col(\"Store_Sales\"))\\\n                .withColumn(\"A_B_C\",when(col(\"Perc\")\u003c\u003d0.80,\"A\").otherwise(when(col(\"Perc\")\u003c\u003d0.95,\"B\").otherwise(\"C\")))\\\n                .withColumn(\"F_M_S\",when(col(\"Days_Sold_Ratio\")\u003e\u003d0.75,\"F\").otherwise(when(col(\"Days_Sold_Ratio\")\u003e\u003d0.25,\"M\").otherwise(\"S\")))\\\n                .select(\"tsm_prod_code\",\"A_B_C\",\"F_M_S\")\n\n################## Sales Calculation #################\n\nD1_Sales \u003d lot_stk_move1.filter(col(\"tsm_cre_date\")\u003d\u003dd0).groupBy(\"tsm_prod_code\").agg(round(sum(\"tsm_qty_total\"),0).alias(\"D0_Sales\"))\nD2_Sales \u003d lot_stk_move1.filter(col(\"tsm_cre_date\")\u003d\u003dd1).groupBy(\"tsm_prod_code\").agg(round(sum(\"tsm_qty_total\"),0).alias(\"D1_Sales\"))\nD8_Sales \u003d lot_stk_move1.filter(col(\"tsm_cre_date\")\u003d\u003dd7).groupBy(\"tsm_prod_code\").agg(round(sum(\"tsm_qty_total\"),0).alias(\"D7_Sales\"))\nAvg_Sales \u003d lot_stk_move1.filter(col(\"tsm_cre_date\").isin([d7,d14,d21,d28])).groupBy(\"tsm_prod_code\",\"tsm_cre_date\").agg(sum(\"tsm_qty_total\").alias(\"Tot_Sales\"))\\\n                         .groupBy(\"tsm_prod_code\").agg(round(avg(\"Tot_Sales\"),0).alias(\"Avg_Sales\"))\n\nbroadcast(D1_Sales)\nbroadcast(D2_Sales)\nbroadcast(D8_Sales)\nbroadcast(Product_Class)\nbroadcast(Products)\nbroadcast(Master)\n\n\nSales \u003d Avg_Sales.join(D8_Sales,\"tsm_prod_code\",\"leftouter\")\\\n                 .join(D2_Sales,\"tsm_prod_code\",\"leftouter\")\\\n                 .join(D1_Sales,\"tsm_prod_code\",\"leftouter\")\\\n                 .join(Product_Class,\"tsm_prod_code\",\"leftouter\")\\\n                 .join(Products,\"tsm_prod_code\",\"leftouter\")\\\n                 .join(Master,\"prod_div_code\",\"leftouter\").fillna(0)\\\n                 .withColumn(\"Rule_1\",when(col(\"D0_Sales\") \u003c 0.15*col(\"Avg_Sales\"), 1).otherwise(0))\\\n                 .withColumn(\"Rule_2\",when(col(\"D0_Sales\") \u003c 0.15*col(\"D7_Sales\"), 1).otherwise(0))\\\n                 .withColumn(\"Rule_3\",when(col(\"D0_Sales\") \u003c 0.15*col(\"D1_Sales\"), 1).otherwise(0))\\\n                 .withColumn(\"Rules_Broken\",col(\"Rule_1\")+col(\"Rule_2\")+col(\"Rule_3\"))\\\n                 .withColumn(\"Sales_Alert\",when(col(\"Rules_Broken\")\u003e\u003d2,1).otherwise(0))\\\n                 .withColumn(\"Create_Date\",lit(d0))\\\n                 .withColumnRenamed(\"tsm_prod_code\",\"Prod_Code\")\n\n#Sales.printSchema()\n#Sales.orderBy(desc(\"Avg_Sales\")).show(50,False)\nSales.cache()\nprint Sales.count()",
      "user": "info@zedeyelabs.com",
      "dateUpdated": "Apr 24, 2018 11:14:10 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "runtimeInfos": {
        "jobUrl": {
          "propertyName": "jobUrl",
          "label": "JOB UI",
          "tooltip": "View in Spark web UI",
          "group": "spark",
          "values": [
            "https://api.qubole.com/cluster-proxy?encodedUrl\u003dhttp%3A%2F%2F172.31.57.131%3A8088%2Fproxy%2Fapplication_1524568242538_0001/jobs/job?spark\u003dtrue\u0026id\u003d0"
          ],
          "interpreterSettingId": "2DCN2CQ97538851523344882186"
        }
      },
      "version": "v0",
      "jobName": "paragraph_1523181345478_-437663655",
      "id": "20180408-095545_1228218362_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "ERROR",
        "type": "TEXT",
        "msg": "Traceback (most recent call last):\n  File \"/tmp/zeppelin_pyspark-5192560507451224997.py\", line 299, in \u003cmodule\u003e\n    raise Exception(traceback.format_exc())\nException: Traceback (most recent call last):\n  File \"/tmp/zeppelin_pyspark-5192560507451224997.py\", line 292, in \u003cmodule\u003e\n    exec(code)\n  File \"\u003cstdin\u003e\", line 13, in \u003cmodule\u003e\n  File \"/usr/lib/spark/python/pyspark/sql/dataframe.py\", line 427, in count\n    return int(self._jdf.count())\n  File \"/usr/lib/spark/python/lib/py4j-0.10.4-src.zip/py4j/java_gateway.py\", line 1131, in __call__\n    answer \u003d self.gateway_client.send_command(command)\n  File \"/usr/lib/spark/python/lib/py4j-0.10.4-src.zip/py4j/java_gateway.py\", line 883, in send_command\n    response \u003d connection.send_command(command)\n  File \"/usr/lib/spark/python/lib/py4j-0.10.4-src.zip/py4j/java_gateway.py\", line 1028, in send_command\n    answer \u003d smart_decode(self.stream.readline()[:-1])\n  File \"/usr/lib64/python2.7/socket.py\", line 451, in readline\n    data \u003d self._sock.recv(self._rbufsize)\n  File \"/usr/lib/spark/python/pyspark/context.py\", line 237, in signal_handler\n    raise KeyboardInterrupt()\nKeyboardInterrupt\n\n"
      },
      "dateCreated": "Apr 8, 2018 9:55:45 AM",
      "dateStarted": "Apr 24, 2018 11:14:10 AM",
      "dateFinished": "Apr 24, 2018 11:18:19 AM",
      "status": "ERROR",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Low Sales Products",
      "text": "%pyspark\n\nSales.filter(\"Avg_Sales\u003e10\").groupBy(\"A_B_C\",\"F_M_S\").agg(count(\"*\").alias(\"cnt\"),sum(\"Sales_Alert\").alias(\"Alert\")).orderBy(\"A_B_C\",\"F_M_S\").show(100)",
      "user": "info@zedeyelabs.com",
      "dateUpdated": "Apr 19, 2018 10:47:28 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523283833872_1991529385",
      "id": "20180409-142353_1205348469_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "+-----+-----+---+-----+\n|A_B_C|F_M_S|cnt|Alert|\n+-----+-----+---+-----+\n|    A|    F|323|   17|\n|    A|    M| 64|   26|\n|    A|    S|  6|    2|\n|    B|    F| 14|    4|\n|    B|    M| 48|   24|\n|    B|    S| 18|    8|\n|    C|    F|  1|    0|\n|    C|    M|  8|    5|\n|    C|    S| 19|    9|\n+-----+-----+---+-----+\n\n"
      },
      "dateCreated": "Apr 9, 2018 2:23:53 PM",
      "dateStarted": "Apr 19, 2018 10:47:28 AM",
      "dateFinished": "Apr 19, 2018 10:47:31 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Alert Products",
      "text": "%pyspark\n\nAlert \u003d Sales.filter(\"(A_B_C\u003d\u0027A\u0027 and F_M_S in (\u0027F\u0027,\u0027M\u0027)) or (A_B_C\u003d\u0027B\u0027 and F_M_S\u003d\u0027F\u0027)\")\\\n             .filter(\"Avg_Sales\u003e10\").filter(\"Sales_Alert\u003d\u003d1\")\\\n             .filter(\"Prod_Description NOT LIKE \u0027%OFFER%\u0027 AND Prod_Description NOT LIKE \u0027%@%\u0027 AND Prod_Description NOT LIKE \u0027%OFF PRICE%\u0027 AND Prod_Description NOT LIKE                          \u0027%+%\u0027 AND Prod_Description NOT LIKE \u0027%SPECIAL PRICE%\u0027 AND Prod_Description NOT LIKE \u0027%@SP %\u0027 AND Prod_Description NOT LIKE \u0027%PROMO%\u0027                                         AND Prod_Description NOT LIKE \u0027%DISCOUNT%\u0027 AND Prod_Description NOT LIKE \u0027%\\% OFF%\u0027 AND Prod_Description NOT LIKE \u0027%\\% OFF%\u0027                                                AND Prod_Description NOT LIKE \u0027%\\% EXTRA%\u0027 AND Prod_Description NOT LIKE \u0027%\\%EXTRA%\u0027\")\\\n             .orderBy(\"Prod_Division\",desc(\"Avg_Sales\"))\n\ndf \u003d Alert.select(\"Prod_Code\",\"Prod_Description\",\"Prod_Division\",\"D0_Sales\",\"D1_Sales\",\"D7_Sales\",\"Avg_Sales\")\n\ndf.show(100,truncate\u003dFalse)",
      "user": "info@zedeyelabs.com",
      "dateUpdated": "Apr 19, 2018 10:47:31 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523523949132_1425759409",
      "id": "20180412-090549_1720663037_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "+------------+--------------------------------------------------+---------------------+--------+--------+--------+---------+\n|Prod_Code   |Prod_Description                                  |Prod_Division        |D0_Sales|D1_Sales|D7_Sales|Avg_Sales|\n+------------+--------------------------------------------------+---------------------+--------+--------+--------+---------+\n|011105000052|HAYAT LITE FRYING OIL 1.8LTR                      |FMCG                 |1.0     |69.0    |95.0    |75.0     |\n|012423000075|SPRITE REGULAR CAN 150ML                          |FMCG                 |0.0     |31.0    |120.0   |61.0     |\n|012423000018|PEPSI CAN S/S 150ML                               |FMCG                 |1.0     |2.0     |151.0   |52.0     |\n|012901000158|MAPCO PAPER TISSUE 200X2PLY                       |FMCG                 |0.0     |4.0     |49.0    |50.0     |\n|012421000005|AL AIN MINERAL WATER 250ML                        |FMCG                 |0.0     |0.0     |48.0    |48.0     |\n|012421000001|MASAFI MINERAL WATER SHRINK WRAP 1.5L             |FMCG                 |0.0     |0.0     |60.0    |44.0     |\n|012801000008|SUPER TOUCH GENERAL PURPOSE CLEANER DETERGENT 5LTR|FMCG                 |0.0     |0.0     |34.0    |34.0     |\n|011006000107|ORION CHEWING GUM STRAWBERRY                      |FMCG                 |0.0     |20.0    |0.0     |32.0     |\n|011805000105|AL HAMRA EVAPORATED MILK 410ML                    |FMCG                 |3.0     |5.0     |31.0    |31.0     |\n|011002000588|ADORE FIORI CHOCOLATE 36GM                        |FMCG                 |1.0     |31.0    |25.0    |30.0     |\n|012707000088|GRAND BLEACH 1US GALLON                           |FMCG                 |0.0     |5.0     |73.0    |26.0     |\n|011805000010|RAINBOW EVAPORATED MILK CARDAMOM 6 OZ             |FMCG                 |0.0     |19.0    |3.0     |24.0     |\n|011501000032|SONA JAGGERY 500GM                                |FMCG                 |0.0     |4.0     |8.0     |19.0     |\n|010301000191|ALI TEA CLASSIC 3 IN 1 WITH GINGER                |FMCG                 |0.0     |2.0     |0.0     |19.0     |\n|010301000037|NESTLE NESCAFE JAR 200 GM (N1) NS081              |FMCG                 |0.0     |0.0     |31.0    |18.0     |\n|012901000162|AYIN FACIAL TISSUE 200\u0027S                          |FMCG                 |0.0     |0.0     |25.0    |17.0     |\n|012912000008|ZAF PLASTIC GLASSES 50\u0027S                          |FMCG                 |2.0     |20.0    |0.0     |14.0     |\n|012911000008|AL AREEN LD GARBAGE BAG 105*125(60 MICRO)         |FMCG                 |0.0     |0.0     |9.0     |12.0     |\n|011002000441|CADBURY DAIRY MILK 37GM                           |FMCG                 |0.0     |24.0    |24.0    |12.0     |\n|040801000056|SADIA WHOLE CHICKEN 1000GM                        |FRESH FOOD           |4.0     |48.0    |53.0    |62.0     |\n|040801000220|SEARA WHOLE CHICKEN 1200GM                        |FRESH FOOD           |1.0     |31.0    |15.0    |15.0     |\n|4311        |SWEET SMILE S/T CHOCOLATE ASSTD KG                |FRESH FOOD           |1.0     |0.0     |25.0    |13.0     |\n|360200000451|SCI TECH SMART WATCH                              |HEAVY HOUSE HOLD     |0.0     |0.0     |23.0    |23.0     |\n|110829000009|ALBA RADO BOX FILE BROAD                          |LIGHT HOUSE HOLD     |0.0     |0.0     |50.0    |50.0     |\n|110805000322|CELLO SOFT TIP PEN                                |LIGHT HOUSE HOLD     |1.0     |13.0    |0.0     |29.0     |\n|240101000017|KITCHEN MARK 3801 MELAMINE DINNER PLATE 10\"       |LIGHT HOUSE HOLD     |0.0     |1.0     |0.0     |26.0     |\n|110805000193|CELLO FINEGRIP DISPLAY                            |LIGHT HOUSE HOLD     |2.0     |1.0     |53.0    |15.0     |\n|110891000075|BELL N-129 NAIL CLIPPER LARGE                     |LIGHT HOUSE HOLD     |1.0     |2.0     |17.0    |13.0     |\n|900102000001|ETISALAT RECHARGE CARD AED:25.00/-                |PHONE CARDS AND SALIK|0.0     |7.0     |38.0    |43.0     |\n|120126000280|OUT DOOR MCS5 MEN\u0027S CROP SOCKS 1X5                |TEXTILES             |0.0     |16.0    |41.0    |29.0     |\n|121203000070|GALAXY SPONGE PILLOW                              |TEXTILES             |0.0     |5.0     |0.0     |26.0     |\n|160401000072|AL AJMI MENS FANCY JEANS SLIM FIT PF02-6          |TEXTILES             |0.0     |0.0     |6.0     |25.0     |\n|161100000326|OUT FIT OFT-AP21 MENS T-SHIRT V/N                 |TEXTILES             |2.0     |6.0     |15.0    |25.0     |\n|120622000145|AGREE NEW BORN PANTY 103114/1                     |TEXTILES             |0.0     |1.0     |9.0     |11.0     |\n+------------+--------------------------------------------------+---------------------+--------+--------+--------+---------+\n\n"
      },
      "dateCreated": "Apr 12, 2018 9:05:49 AM",
      "dateStarted": "Apr 19, 2018 10:47:31 AM",
      "dateFinished": "Apr 19, 2018 10:47:33 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Email UDF",
      "text": "%pyspark\n\nimport csv\nfrom tabulate import tabulate\nfrom email.mime.multipart import MIMEMultipart\nfrom email.mime.text import MIMEText\nfrom email.mime.application import MIMEApplication\nimport smtplib\n\ndef email_alert_udf(me,password,you,cc,subject,text,html,df,d0):\n\tlist \u003ddf.rdd.map(lambda row: [str(c) for c in row]).collect()\n\tdata \u003d [df.columns]+list\n\ttext \u003d text.format(table\u003dtabulate(data, headers\u003d\"firstrow\", tablefmt\u003d\"grid\"))\n\thtml \u003d html.format(table\u003dtabulate(data, headers\u003d\"firstrow\", tablefmt\u003d\"html\"))\n\n\tmessage \u003d MIMEMultipart(\"alternative\", None, [MIMEText(text),MIMEText(html,\u0027html\u0027)])\n\n\tmessage[\u0027Subject\u0027] \u003d subject\n\tmessage[\u0027From\u0027] \u003d me\n\tmessage[\u0027To\u0027] \u003d \", \".join(you)\n\tmessage[\u0027Cc\u0027] \u003d \", \".join(cc)\n\t\n\twith open(\u0027/tmp/some-file.csv\u0027, \u0027wt\u0027) as fw:\n\t    writer \u003d csv.writer(fw)\n\t    writer.writerows(data)\n\t\n\tpart \u003d MIMEApplication(open(\u0027/tmp/some-file.csv\u0027, \u0027r\u0027).read())\n\tpart[\u0027Content-Disposition\u0027] \u003d \u0027attachment; filename\u003d%s\u0027 % \"Products List : \"+str(d0.strftime(\u0027%d-%m-%Y\u0027))+\".csv\"\n\tmessage.attach(part)\n\t\n\tserver \u003d \u0027smtp.office365.com:587\u0027\n\tserver \u003d smtplib.SMTP(server)\n\tserver.ehlo()\n\tserver.starttls()\n\tserver.login(me, password)\n\tserver.sendmail(me, you+cc, message.as_string())\n\tserver.quit()\n\tprint(\"Email Sent Successfully\")",
      "user": "40993",
      "dateUpdated": "Apr 12, 2018 9:08:30 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523285643679_1752004843",
      "id": "20180409-145403_1003241807_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": ""
      },
      "dateCreated": "Apr 9, 2018 2:54:03 PM",
      "dateStarted": "Apr 19, 2018 4:58:40 AM",
      "dateFinished": "Apr 19, 2018 4:58:42 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Sales Alarm Email",
      "text": "%pyspark\n\nme \u003d \u0027rinaz.belhaj@zedeyelabs.com\u0027\npassword \u003d \u0027grand@123\u0027\nyou \u003d [\u0027rahul.malani@zedeyelabs.com\u0027,\u0027sarvesh.rao@zedeyelabs.com\u0027]\ncc \u003d [\u0027rinazbelhaj@gmail.com\u0027]\n\nsubject \u003d \"Sales Alarm for Non Performing SKUs - GCity\"\n\ntext \u003d \"\"\"\nHello Store Managers, \n\nPlease find the below list of fast moving and high value SKUs whose sales performance is not as per the expectation on \u003cb\u003e\"\"\"+str(d0.strftime(\u0027%A : %d-%b-%Y\u0027))+\"\"\"\u003c/b\u003e. Kindly have a look at it and respond with reasons behind poor performance.\n\nNote:\nD0_Sales - Yesterday\u0027s [\"\"\"+d0.strftime(\u0027%A\u0027)+\"\"\"]  Sales Quantity\nD1_Sales - Day Before Yesterday\u0027s [\"\"\"+d1.strftime(\u0027%A\u0027)+\"\"\"] Sales Quantity\nD7_Sales - Last Week \"\"\"+d7.strftime(\u0027%A\u0027)+\"\"\"\u0027s Sales Quantity\nAvg_Sales - Average Sales Quantity of Last 4 \"\"\"+d7.strftime(\u0027%A\u0027)+\"\"\"s\n\n{table}\n\nRegards,\nZedeye Labs\n\"\"\"\n\nhtml \u003d \"\"\"\n\u003chtml\u003e\n\u003chead\u003e\n\u003cstyle\u003e \n  table, th, td {{ border: 1px solid black; border-collapse: collapse; }}\n  th, td {{ padding: 5px; }}\n\u003c/style\u003e\n\u003c/head\u003e\n\u003cbody\u003e\n\u003cp\u003e\u003cb\u003eHello Store Managers,\u003c/b\u003e\u003c/p\u003e\n\u003cp\u003ePlease find the below list of fast moving and high value SKUs whose sales performance on \u003cb\u003e\"\"\"+str(d0.strftime(\u0027%A : %d-%b-%Y\u0027))+\"\"\"\u003c/b\u003e was not as per the expectation. Kindly have a look at it and respond with reasons behind poor performance.\u003c/p\u003e\n\u003cp\u003e\u003cb\u003eNote:\u003c/b\u003e\u003c/p\u003e\n\u003cp\u003e\u003cb\u003eD0_Sales - Yesterday\u0027s [\"\"\"+d0.strftime(\u0027%A\u0027)+\"\"\"]  Sales Quantity\u003c/b\u003e\n\u003cbr /\u003e\u003cb\u003eD1_Sales - Day Before Yesterday\u0027s [\"\"\"+d1.strftime(\u0027%A\u0027)+\"\"\"] Sales Quantity\u003c/b\u003e\n\u003cbr /\u003e\u003cb\u003eD7_Sales - Last Week \"\"\"+d7.strftime(\u0027%A\u0027)+\"\"\"\u0027s Sales Quantity\u003c/b\u003e\n\u003cbr /\u003e\u003cb\u003eAvg_Sales - Average Sales Quantity of Last 4 \"\"\"+d7.strftime(\u0027%A\u0027)+\"\"\"s\u003c/b\u003e\u003c/p\u003e\n\u003cbr /\u003e\n\n{table}\n\n\u003cp\u003e\u003cb\u003eRegards,\u003c/b\u003e\n\u003cbr /\u003e\u003cb\u003eZedeye Labs\u003c/b\u003e\u003c/p\u003e\n\u003c/body\u003e\n\u003c/html\u003e\n\"\"\"\n \nAlert \u003d Sales.filter(\"(A_B_C\u003d\u0027A\u0027 and F_M_S in (\u0027F\u0027,\u0027M\u0027)) or (A_B_C\u003d\u0027B\u0027 and F_M_S\u003d\u0027F\u0027)\")\\\n             .filter(\"Avg_Sales\u003e10\").filter(\"Sales_Alert\u003d\u003d1\")\\\n             .filter(\"Prod_Description NOT LIKE \u0027%OFFER%\u0027 AND Prod_Description NOT LIKE \u0027%@%\u0027 AND Prod_Description NOT LIKE \u0027%OFF PRICE%\u0027 AND Prod_Description NOT LIKE                        \u0027%+%\u0027 AND Prod_Description NOT LIKE \u0027%SPECIAL PRICE%\u0027 AND Prod_Description NOT LIKE \u0027%@SP %\u0027 AND Prod_Description NOT LIKE \u0027%PROMO%\u0027                                       AND Prod_Description NOT LIKE \u0027%DISCOUNT%\u0027 AND Prod_Description NOT LIKE \u0027%\\% OFF%\u0027 AND Prod_Description NOT LIKE \u0027%\\% OFF%\u0027                                               AND Prod_Description NOT LIKE \u0027%\\% EXTRA%\u0027 AND Prod_Description NOT LIKE \u0027%\\%EXTRA%\u0027\")\\\n             .orderBy(\"Prod_Division\",desc(\"Avg_Sales\"))\n \ndf \u003d Alert.select(\"Prod_Code\",\"Prod_Description\",\"Prod_Division\",\"D0_Sales\",\"D1_Sales\",\"D7_Sales\",\"Avg_Sales\")\n\nif(df.count()\u003e0):\n    email_alert_udf(me,password,you,cc,subject,text,html,df,d0)\n    out_path \u003d \"s3://zedeyelabs/Projects/Sales_Alarm/Dubai/Gcity/\"+ str(d0)[0:4] +\"/\" + str(d0)[5:7]+\"/\"+str(d0)[8:10]+\"/\"\n    Alert.write.mode(\"overwrite\").parquet(out_path)\n    print(\"Files Written to S3\")\nelse:\n    print(\"No Mail Sent\")\n\n#Sales.unpersist()\n#lot_stk_move1.unpersist()\nprint(\"\")",
      "user": "40993",
      "dateUpdated": "Apr 16, 2018 7:10:21 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523254275429_-1645375496",
      "id": "20180409-061115_43418542_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "Email Sent Successfully\nFiles Written to S3\n\n"
      },
      "dateCreated": "Apr 9, 2018 6:11:15 AM",
      "dateStarted": "Apr 19, 2018 4:58:42 AM",
      "dateFinished": "Apr 19, 2018 4:59:11 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    },
    {
      "title": "Escalation Mail to Higher Management",
      "text": "%pyspark\n\nyou \u003d [\u0027rahul.malani@zedeyelabs.com\u0027,\u0027sarvesh.rao@zedeyelabs.com\u0027]\ncc \u003d [\u0027rinazbelhaj@gmail.com\u0027]\n\nsubject \u003d \"Escalation : Sales Alarm for Non Performing SKUs - GCity\"\n\ntext \u003d \"\"\"\nDear Anvar Sir,\n\nPlease find the below list of fast moving and high value SKUs whose sales performance was poor for last 6 days. Kindly discuss the same with the concerned store manager.\n\nNote:\n6Day_Avg_Sales - Last 6 Days Average Sales Quantity\nAvg_Sales - Last 28 Days Average Sales Quantity\n\n{table}\n\nRegards,\nZedeye Labs\n\"\"\"\n\nhtml \u003d \"\"\"\n\u003chtml\u003e\n\u003chead\u003e\n\u003cstyle\u003e \n  table, th, td {{ border: 1px solid black; border-collapse: collapse; }}\n  th, td {{ padding: 5px; }}\n\u003c/style\u003e\n\u003c/head\u003e\n\u003cbody\u003e\n\u003cp\u003e\u003cb\u003eDear Anvar Sir,\u003c/b\u003e\u003c/p\u003e\n\u003cp\u003ePlease find the below list of fast moving and high value SKUs whose sales performance was poor for last 6 days. Kindly discuss the same with the concerned store manager.\u003c/p\u003e\n\u003cp\u003e\u003cb\u003eNote:\u003c/b\u003e\u003c/p\u003e\n\u003cp\u003e\u003cb\u003e6Day_Avg_Sales - Last 6 Days Average Sales Quantity\u003c/b\u003e\n\u003cbr /\u003e\u003cb\u003eAvg_Sales - Last 28 Days Average Sales Quantity\u003c/b\u003e\u003c/p\u003e\n\u003cbr /\u003e\n\n{table}\n\n\u003cp\u003e\u003cb\u003eRegards,\u003c/b\u003e\n\u003cbr /\u003e\u003cb\u003eZedeye Labs\u003c/b\u003e\u003c/p\u003e\n\u003c/body\u003e\n\u003c/html\u003e\n\"\"\"\n\nin_path \u003d \"s3://zedeyelabs/Projects/Sales_Alarm/Dubai/Gcity/*/*/*/\"\n\nAlarm_3 \u003d spark.read.parquet(in_path).filter(col(\"Create_Date\")\u003e\u003dd6)\\\n                                     .groupBy(\"Prod_Code\",\"Prod_Description\",\"Prod_Division\")\\\n                                     .agg(sum(\"Sales_Alert\").alias(\"Alarm\"),avg(\"D0_Sales\").alias(\"6Day_Avg_Sales\"),avg(\"Avg_Sales\").alias(\"Avg_Sales\"))\\\n                                     .filter(\"Alarm\u003e\u003d6\").drop(\"Alarm\")\\\n                                     .orderBy(\"Prod_Division\",desc(\"Avg_Sales\"))\n\nAlarm_3.show(5)\n\nif(Alarm_3.count()\u003e0):\n    print(\"Escalated today\")\n    email_alert_udf(me,password,you,cc,subject,text,html,Alarm_3,d0)\nelse:\n    print(\"No Escalation today\")",
      "user": "40993",
      "dateUpdated": "Apr 12, 2018 9:08:45 AM",
      "config": {
        "colWidth": 12.0,
        "graph": {
          "mode": "table",
          "height": 300.0,
          "optionOpen": false,
          "keys": [],
          "values": [],
          "groups": [],
          "scatter": {}
        },
        "enabled": true,
        "editorMode": "ace/mode/python",
        "title": true
      },
      "settings": {
        "params": {},
        "forms": {}
      },
      "version": "v0",
      "jobName": "paragraph_1523267681699_272113304",
      "id": "20180409-095441_523403571_q_AVXJ1HNZCT1524132517",
      "result": {
        "code": "SUCCESS",
        "type": "TEXT",
        "msg": "+---------+----------------+-------------+--------------+---------+\n|Prod_Code|Prod_Description|Prod_Division|6Day_Avg_Sales|Avg_Sales|\n+---------+----------------+-------------+--------------+---------+\n+---------+----------------+-------------+--------------+---------+\n\nNo Escalation today\n"
      },
      "dateCreated": "Apr 9, 2018 9:54:41 AM",
      "dateStarted": "Apr 19, 2018 4:58:42 AM",
      "dateFinished": "Apr 19, 2018 4:59:36 AM",
      "status": "FINISHED",
      "progressUpdateIntervalMs": 500
    }
  ],
  "name": "Sales Alarm - GCity - Clone",
  "id": "AVXJ1HNZCT1524132517",
  "angularObjects": {
    "2DCN2CQ97538851523344882186:shared_process": [],
    "2DCMU6C6C538851523344882315:shared_process": [],
    "2DCPFSF9J538851523344882362:shared_process": [],
    "2DDPX2XX9538851523344882272:shared_process": []
  },
  "config": {
    "isDashboard": false,
    "looknfeel": "default",
    "releaseresource": true,
    "cronExecutingUser": "40993",
    "cron_updated_by_useremail": "info@zedeyelabs.com"
  },
  "info": {},
  "source": "FCN"
}