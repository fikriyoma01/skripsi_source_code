#  Copyright 2022 Diagnostic Image Analysis Group, Radboudumc, Nijmegen, The Netherlands
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import argparse
import json
from pathlib import Path
from typing import Any, Dict, Optional


def export_splits(
    train_splits: Optional[Dict[str, Any]] = None,
    valid_splits: Optional[Dict[str, Any]] = None,
    output_folder: Optional[str] = None,
) -> None:
    """Export dataset configuration files to disk"""
    if output_folder is None:
        parser = argparse.ArgumentParser(description='Command Line Arguments')
        parser.add_argument("-o", "--output", type=str, required=True,
                            help="Output path to store cross-validation splits")
        args = parser.parse_args()
        output_folder = args.output

    output_folder: Path = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    if train_splits is not None:
        for fold, ds_config in train_splits.items():
            path = output_folder / f"ds-config-train-fold-{fold}.json"
            print(f"Saving training fold {fold} with {len(ds_config['subject_list'])} cases to {path}")
            with open(path, "w") as fp:
                json.dump(ds_config, fp, indent=4)

    if valid_splits is not None:
        for fold, ds_config in valid_splits.items():
            path = output_folder / f"ds-config-valid-fold-{fold}.json"
            print(f"Saving training fold {fold} with {len(ds_config['subject_list'])} cases to {path}")
            with open(path, "w") as fp:
                json.dump(ds_config, fp, indent=4)


subject_list_annotated = [
    '10000_1000000',
    '10001_1000001',
    '10002_1000002',
    '10003_1000003',
    '10004_1000004',
    '10005_1000005',
    '10006_1000006',
    '10007_1000007',
    '10009_1000009',
    '10010_1000010',
    '10011_1000011',
    '10012_1000012',
    '10014_1000014',
    '10015_1000015',
    '10016_1000016',
    '10017_1000017',
    '10018_1000018',
    '10019_1000019',
    '10020_1000020',
    '10021_1000021',
    '10022_1000022',
    '10023_1000023',
    '10024_1000024',
    '10025_1000025',
    '10026_1000026',
    '10027_1000027',
    '10028_1000028',
    '10030_1000030',
    '10031_1000031',
    '10032_1000032',
    '10033_1000033',
    '10034_1000034',
    '10035_1000035',
    '10037_1000037',
    '10038_1000038',
    '10039_1000039',
    '10040_1000040',
    '10041_1000041',
    '10042_1000042',
    '10043_1000043',
    '10045_1000045',
    '10046_1000046',
    '10047_1000047',
    '10048_1000048',
    '10049_1000049',
    '10051_1000051',
    '10052_1000052',
    '10054_1000054',
    '10055_1000055',
    '10056_1000056',
    '10057_1000057',
    '10058_1000058',
    '10059_1000059',
    '10060_1000060',
    '10061_1000061',
    '10062_1000062',
    '10063_1000063',
    '10064_1000064',
    '10065_1000065',
    '10066_1000066',
    '10067_1000067',
    '10068_1000068',
    '10069_1000069',
    '10070_1000070',
    '10071_1000071',
    '10072_1000072',
    '10073_1000073',
    '10074_1000074',
    '10075_1000075',
    '10076_1000076',
    '10077_1000077',
    '10078_1000078',
    '10079_1000079',
    '10080_1000080',
    '10081_1000081',
    '10082_1000082',
    '10083_1000083',
    '10084_1000084',
    '10085_1000085',
    '10086_1000086',
    '10087_1000087',
    '10088_1000088',
    '10089_1000089',
    '10090_1000090',
    '10091_1000091',
    '10092_1000092',
    '10093_1000093',
    '10095_1000095',
    '10096_1000096',
    '10097_1000097',
    '10098_1000098',
    '10099_1000099',
    '10101_1000101',
    '10102_1000102',
    '10103_1000103',
    '10105_1000105',
    '10107_1000107',
    '10108_1000108',
    '10109_1000109',
    '10110_1000110',
    '10111_1000111',
    '10113_1000113',
    '10114_1000114',
    '10115_1000115',
    '10116_1000116',
    '10117_1000117',
    '10118_1000118',
    '10119_1000119',
    '10120_1000120',
    '10121_1000121',
    '10122_1000122',
    '10123_1000123',
    '10124_1000124',
    '10125_1000125',
    '10126_1000126',
    '10127_1000127',
    '10128_1000128',
    '10129_1000129',
    '10129_1000130',
    '10130_1000131',
    '10131_1000132',
    '10131_1000133',
    '10133_1000135',
    '10134_1000136',
    '10136_1000138',
    '10137_1000139',
    '10138_1000140',
    '10139_1000141',
    '10141_1000143',
    '10142_1000144',
    '10143_1000145',
    '10144_1000146',
    '10145_1000147',
    '10146_1000148',
    '10147_1000149',
    '10149_1000151',
    '10150_1000152',
    '10151_1000153',
    '10152_1000154',
    '10153_1000155',
    '10153_1000156',
    '10154_1000157',
    '10155_1000158',
    '10156_1000159',
    '10157_1000160',
    '10158_1000161',
    '10159_1000162',
    '10160_1000163',
    '10161_1000164',
    '10162_1000165',
    '10163_1000166',
    '10164_1000167',
    '10165_1000168',
    '10166_1000169',
    '10167_1000170',
    '10168_1000171',
    '10169_1000172',
    '10172_1000175',
    '10173_1000176',
    '10174_1000177',
    '10175_1000178',
    '10176_1000179',
    '10177_1000180',
    '10178_1000181',
    '10179_1000182',
    '10180_1000183',
    '10181_1000184',
    '10183_1000186',
    '10184_1000187',
    '10185_1000188',
    '10186_1000189',
    '10187_1000190',
    '10188_1000191',
    '10189_1000192',
    '10190_1000193',
    '10191_1000194',
    '10192_1000195',
    '10193_1000196',
    '10193_1000197',
    '10194_1000198',
    '10195_1000199',
    '10196_1000200',
    '10197_1000201',
    '10198_1000202',
    '10199_1000203',
    '10200_1000204',
    '10201_1000205',
    '10202_1000206',
    '10203_1000207',
    '10204_1000208',
    '10205_1000209',
    '10206_1000210',
    '10207_1000211',
    '10208_1000212',
    '10210_1000214',
    '10211_1000215',
    '10213_1000217',
    '10215_1000219',
    '10216_1000220',
    '10217_1000221',
    '10218_1000222',
    '10219_1000223',
    '10220_1000224',
    '10221_1000225',
    '10222_1000226',
    '10223_1000227',
    '10224_1000228',
    '10226_1000230',
    '10227_1000231',
    '10228_1000232',
    '10230_1000234',
    '10231_1000235',
    '10233_1000237',
    '10234_1000238',
    '10237_1000241',
    '10238_1000242',
    '10239_1000243',
    '10240_1000244',
    '10241_1000245',
    '10242_1000246',
    '10243_1000247',
    '10244_1000248',
    '10245_1000249',
    '10246_1000250',
    '10247_1000251',
    '10248_1000252',
    '10249_1000253',
    '10250_1000254',
    '10251_1000255',
    '10252_1000256',
    '10253_1000257',
    '10254_1000258',
    '10255_1000259',
    '10256_1000260',
    '10257_1000261',
    '10258_1000262',
    '10259_1000263',
    '10260_1000264',
    '10261_1000265',
    '10262_1000266',
    '10263_1000267',
    '10264_1000268',
    '10265_1000269',
    '10266_1000270',
    '10267_1000271',
    '10268_1000272',
    '10269_1000273',
    '10270_1000274',
    '10272_1000276',
    '10273_1000277',
    '10274_1000279',
    '10275_1000280',
    '10276_1000281',
    '10277_1000282',
    '10278_1000283',
    '10279_1000284',
    '10281_1000286',
    '10281_1000287',
    '10284_1000290',
    '10285_1000291',
    '10286_1000292',
    '10287_1000293',
    '10288_1000294',
    '10289_1000295',
    '10290_1000296',
    '10291_1000297',
    '10292_1000298',
    '10294_1000300',
    '10295_1000301',
    '10296_1000302',
    '10297_1000303',
    '10298_1000304',
    '10299_1000305',
    '10300_1000306',
    '10301_1000307',
    '10302_1000308',
    '10303_1000309',
    '10304_1000310',
    '10305_1000311',
    '10306_1000312',
    '10307_1000313',
    '10308_1000314',
    '10309_1000315',
    '10310_1000316',
    '10311_1000317',
    '10313_1000319',
    '10314_1000320',
    '10315_1000321',
    '10316_1000322',
    '10317_1000323',
    '10319_1000325',
    '10320_1000326',
    '10321_1000327',
    '10322_1000328',
    '10323_1000329',
    '10325_1000331',
    '10326_1000332',
    '10327_1000333',
    '10328_1000334',
    '10329_1000335',
    '10330_1000336',
    '10331_1000337',
    '10332_1000338',
    '10333_1000339',
    '10335_1000341',
    '10336_1000342',
    '10337_1000343',
    '10338_1000344',
    '10339_1000345',
    '10340_1000346',
    '10341_1000347',
    '10342_1000348',
    '10343_1000349',
    '10344_1000350',
    '10345_1000351',
    '10346_1000352',
    '10347_1000353',
    '10348_1000354',
    '10349_1000355',
    '10350_1000356',
    '10351_1000357',
    '10352_1000358',
    '10353_1000359',
    '10355_1000361',
    '10356_1000362',
    '10357_1000363',
    '10359_1000365',
    '10360_1000366',
    '10361_1000367',
    '10362_1000368',
    '10363_1000369',
    '10364_1000370',
    '10366_1000372',
    '10367_1000373',
    '10368_1000374',
    '10370_1000376',
    '10372_1000378',
    '10373_1000379',
    '10374_1000380',
    '10378_1000384',
    '10379_1000385',
    '10380_1000386',
    '10381_1000387',
    '10382_1000388',
    '10383_1000389',
    '10384_1000390',
    '10385_1000391',
    '10386_1000392',
    '10387_1000393',
    '10388_1000394',
    '10389_1000395',
    '10390_1000396',
    '10391_1000397',
    '10392_1000398',
    '10394_1000400',
    '10395_1000401',
    '10396_1000402',
    '10398_1000404',
    '10401_1000407',
    '10403_1000409',
    '10404_1000410',
    '10404_1000411',
    '10405_1000412',
    '10406_1000413',
    '10407_1000414',
    '10409_1000416',
    '10410_1000417',
    '10411_1000418',
    '10412_1000419',
    '10413_1000420',
    '10414_1000421',
    '10415_1000422',
    '10416_1000423',
    '10417_1000424',
    '10417_1000425',
    '10418_1000426',
    '10419_1000427',
    '10420_1000428',
    '10421_1000429',
    '10422_1000430',
    '10423_1000431',
    '10424_1000432',
    '10425_1000433',
    '10427_1000435',
    '10428_1000436',
    '10429_1000437',
    '10430_1000438',
    '10432_1000440',
    '10434_1000442',
    '10435_1000443',
    '10436_1000444',
    '10437_1000445',
    '10438_1000446',
    '10439_1000447',
    '10440_1000448',
    '10441_1000449',
    '10442_1000450',
    '10443_1000451',
    '10444_1000452',
    '10445_1000453',
    '10446_1000454',
    '10447_1000455',
    '10448_1000456',
    '10449_1000457',
    '10450_1000458',
    '10451_1000459',
    '10452_1000460',
    '10453_1000461',
    '10454_1000462',
    '10455_1000463',
    '10457_1000465',
    '10460_1000468',
    '10461_1000469',
    '10462_1000470',
    '10463_1000471',
    '10466_1000474',
    '10467_1000475',
    '10468_1000476',
    '10469_1000477',
    '10470_1000478',
    '10472_1000480',
    '10473_1000481',
    '10474_1000482',
    '10475_1000483',
    '10476_1000484',
    '10477_1000485',
    '10478_1000486',
    '10479_1000487',
    '10480_1000488',
    '10482_1000490',
    '10483_1000491',
    '10484_1000492',
    '10485_1000493',
    '10486_1000494',
    '10487_1000495',
    '10488_1000496',
    '10489_1000497',
    '10490_1000498',
    '10490_1000499',
    '10491_1000500',
    '10492_1000501',
    '10493_1000502',
    '10495_1000504',
    '10500_1000509',
    '10502_1000511',
    '10503_1000512',
    '10504_1000513',
    '10505_1000514',
    '10506_1000515',
    '10507_1000516',
    '10509_1000518',
    '10511_1000520',
    '10512_1000521',
    '10512_1000522',
    '10513_1000523',
    '10514_1000524',
    '10516_1000526',
    '10518_1000528',
    '10521_1000531',
    '10522_1000532',
    '10523_1000533',
    '10524_1000534',
    '10525_1000535',
    '10526_1000536',
    '10527_1000537',
    '10528_1000538',
    '10529_1000539',
    '10530_1000540',
    '10531_1000541',
    '10532_1000542',
    '10533_1000543',
    '10534_1000544',
    '10535_1000545',
    '10536_1000546',
    '10538_1000548',
    '10539_1000549',
    '10540_1000550',
    '10540_1000551',
    '10541_1000552',
    '10542_1000553',
    '10543_1000554',
    '10544_1000555',
    '10546_1000557',
    '10548_1000559',
    '10548_1000560',
    '10549_1000561',
    '10551_1000563',
    '10552_1000564',
    '10553_1000565',
    '10556_1000568',
    '10557_1000569',
    '10558_1000570',
    '10559_1000571',
    '10561_1000573',
    '10563_1000575',
    '10564_1000576',
    '10566_1000578',
    '10568_1000580',
    '10569_1000581',
    '10570_1000582',
    '10571_1000583',
    '10572_1000584',
    '10573_1000585',
    '10574_1000586',
    '10575_1000587',
    '10576_1000588',
    '10576_1000589',
    '10578_1000591',
    '10579_1000592',
    '10580_1000593',
    '10580_1000594',
    '10581_1000595',
    '10582_1000596',
    '10583_1000597',
    '10585_1000599',
    '10586_1000600',
    '10587_1000601',
    '10588_1000602',
    '10589_1000603',
    '10590_1000604',
    '10591_1000605',
    '10592_1000606',
    '10593_1000607',
    '10594_1000608',
    '10595_1000609',
    '10596_1000610',
    '10597_1000611',
    '10598_1000612',
    '10599_1000613',
    '10600_1000614',
    '10601_1000615',
    '10602_1000616',
    '10603_1000617',
    '10604_1000618',
    '10605_1000619',
    '10607_1000621',
    '10608_1000622',
    '10609_1000623',
    '10610_1000624',
    '10612_1000626',
    '10613_1000627',
    '10614_1000628',
    '10615_1000629',
    '10616_1000630',
    '10617_1000631',
    '10618_1000632',
    '10619_1000633',
    '10620_1000634',
    '10621_1000635',
    '10623_1000637',
    '10624_1000638',
    '10625_1000639',
    '10626_1000640',
    '10627_1000641',
    '10628_1000642',
    '10629_1000643',
    '10629_1000644',
    '10632_1000647',
    '10633_1000648',
    '10634_1000649',
    '10634_1000650',
    '10635_1000651',
    '10637_1000653',
    '10639_1000655',
    '10640_1000656',
    '10641_1000657',
    '10642_1000658',
    '10643_1000659',
    '10645_1000661',
    '10646_1000662',
    '10647_1000663',
    '10648_1000664',
    '10649_1000665',
    '10650_1000666',
    '10653_1000669',
    '10654_1000670',
    '10655_1000671',
    '10656_1000672',
    '10657_1000673',
    '10659_1000675',
    '10662_1000678',
    '10663_1000679',
    '10664_1000680',
    '10665_1000681',
    '10666_1000682',
    '10667_1000683',
    '10668_1000684',
    '10669_1000685',
    '10670_1000686',
    '10671_1000687',
    '10672_1000688',
    '10673_1000689',
    '10674_1000690',
    '10675_1000691',
    '10676_1000692',
    '10677_1000693',
    '10678_1000694',
    '10680_1000696',
    '10681_1000697',
    '10683_1000699',
    '10685_1000701',
    '10687_1000703',
    '10688_1000704',
    '10689_1000705',
    '10691_1000707',
    '10692_1000708',
    '10694_1000710',
    '10695_1000711',
    '10696_1000712',
    '10697_1000713',
    '10698_1000714',
    '10699_1000715',
    '10700_1000716',
    '10702_1000718',
    '10703_1000719',
    '10704_1000720',
    '10705_1000721',
    '10706_1000722',
    '10707_1000723',
    '10708_1000724',
    '10709_1000725',
    '10711_1000727',
    '10712_1000728',
    '10713_1000729',
    '10714_1000730',
    '10715_1000731',
    '10716_1000732',
    '10719_1000735',
    '10720_1000736',
    '10721_1000737',
    '10722_1000738',
    '10723_1000739',
    '10724_1000740',
    '10725_1000741',
    '10726_1000742',
    '10727_1000743',
    '10728_1000744',
    '10729_1000745',
    '10730_1000746',
    '10731_1000747',
    '10732_1000748',
    '10733_1000749',
    '10734_1000750',
    '10735_1000751',
    '10736_1000752',
    '10737_1000753',
    '10738_1000754',
    '10740_1000756',
    '10741_1000757',
    '10743_1000759',
    '10744_1000760',
    '10745_1000761',
    '10746_1000762',
    '10747_1000763',
    '10748_1000764',
    '10749_1000765',
    '10750_1000766',
    '10751_1000767',
    '10752_1000768',
    '10755_1000771',
    '10756_1000772',
    '10757_1000773',
    '10759_1000775',
    '10761_1000777',
    '10762_1000778',
    '10764_1000780',
    '10765_1000781',
    '10766_1000782',
    '10767_1000783',
    '10768_1000784',
    '10769_1000785',
    '10770_1000786',
    '10771_1000787',
    '10774_1000790',
    '10776_1000792',
    '10777_1000793',
    '10778_1000794',
    '10779_1000795',
    '10780_1000796',
    '10782_1000798',
    '10783_1000799',
    '10784_1000800',
    '10785_1000801',
    '10786_1000802',
    '10787_1000803',
    '10788_1000804',
    '10789_1000805',
    '10790_1000806',
    '10791_1000807',
    '10792_1000808',
    '10793_1000809',
    '10794_1000810',
    '10795_1000811',
    '10796_1000812',
    '10798_1000814',
    '10800_1000816',
    '10801_1000817',
    '10802_1000818',
    '10803_1000819',
    '10804_1000820',
    '10805_1000821',
    '10807_1000823',
    '10808_1000824',
    '10809_1000825',
    '10812_1000828',
    '10813_1000829',
    '10814_1000830',
    '10815_1000831',
    '10816_1000832',
    '10817_1000833',
    '10818_1000834',
    '10819_1000835',
    '10820_1000836',
    '10821_1000837',
    '10822_1000838',
    '10823_1000839',
    '10824_1000840',
    '10825_1000841',
    '10826_1000842',
    '10828_1000844',
    '10829_1000845',
    '10830_1000846',
    '10831_1000847',
    '10832_1000848',
    '10833_1000849',
    '10834_1000850',
    '10835_1000851',
    '10836_1000852',
    '10838_1000854',
    '10839_1000855',
    '10840_1000856',
    '10841_1000857',
    '10842_1000858',
    '10843_1000859',
    '10844_1000860',
    '10846_1000862',
    '10847_1000863',
    '10848_1000864',
    '10849_1000865',
    '10850_1000866',
    '10851_1000867',
    '10853_1000869',
    '10854_1000870',
    '10855_1000871',
    '10858_1000874',
    '10859_1000875',
    '10860_1000876',
    '10861_1000877',
    '10863_1000879',
    '10864_1000880',
    '10866_1000882',
    '10867_1000883',
    '10868_1000884',
    '10869_1000885',
    '10870_1000886',
    '10871_1000887',
    '10872_1000888',
    '10874_1000890',
    '10876_1000892',
    '10877_1000893',
    '10878_1000894',
    '10879_1000895',
    '10880_1000896',
    '10881_1000897',
    '10884_1000900',
    '10885_1000901',
    '10886_1000902',
    '10887_1000903',
    '10888_1000904',
    '10891_1000907',
    '10892_1000908',
    '10893_1000909',
    '10895_1000911',
    '10896_1000912',
    '10897_1000913',
    '10898_1000914',
    '10899_1000915',
    '10901_1000917',
    '10902_1000918',
    '10905_1000921',
    '10905_1000922',
    '10906_1000923',
    '10907_1000924',
    '10908_1000925',
    '10910_1000927',
    '10911_1000928',
    '10912_1000929',
    '10913_1000930',
    '10914_1000931',
    '10915_1000932',
    '10916_1000933',
    '10917_1000934',
    '10918_1000935',
    '10919_1000936',
    '10920_1000937',
    '10921_1000938',
    '10922_1000939',
    '10923_1000940',
    '10924_1000941',
    '10925_1000942',
    '10926_1000943',
    '10927_1000944',
    '10928_1000945',
    '10929_1000946',
    '10930_1000947',
    '10931_1000948',
    '10932_1000949',
    '10933_1000950',
    '10934_1000951',
    '10935_1000952',
    '10936_1000953',
    '10936_1000954',
    '10936_1000955',
    '10937_1000956',
    '10938_1000957',
    '10939_1000958',
    '10940_1000959',
    '10941_1000960',
    '10942_1000961',
    '10944_1000963',
    '10945_1000964',
    '10946_1000965',
    '10947_1000966',
    '10948_1000967',
    '10949_1000968',
    '10950_1000969',
    '10951_1000970',
    '10952_1000971',
    '10953_1000972',
    '10954_1000973',
    '10955_1000974',
    '10957_1000976',
    '10958_1000977',
    '10959_1000978',
    '10960_1000979',
    '10961_1000980',
    '10962_1000981',
    '10963_1000982',
    '10964_1000983',
    '10966_1000985',
    '10967_1000986',
    '10968_1000987',
    '10969_1000988',
    '10970_1000989',
    '10971_1000990',
    '10972_1000991',
    '10973_1000992',
    '10974_1000993',
    '10975_1000994',
    '10977_1000996',
    '10978_1000997',
    '10979_1000998',
    '10980_1000999',
    '10981_1001000',
    '10982_1001001',
    '10983_1001002',
    '10984_1001003',
    '10985_1001004',
    '10986_1001005',
    '10987_1001006',
    '10988_1001007',
    '10989_1001008',
    '10990_1001009',
    '10992_1001011',
    '10994_1001013',
    '10996_1001015',
    '10997_1001016',
    '10998_1001017',
    '10999_1001018',
    '11000_1001019',
    '11001_1001020',
    '11002_1001021',
    '11003_1001022',
    '11004_1001023',
    '11004_1001024',
    '11005_1001025',
    '11006_1001026',
    '11007_1001027',
    '11008_1001028',
    '11010_1001030',
    '11011_1001031',
    '11012_1001032',
    '11013_1001033',
    '11014_1001034',
    '11015_1001035',
    '11016_1001036',
    '11017_1001037',
    '11018_1001038',
    '11019_1001039',
    '11020_1001040',
    '11021_1001041',
    '11022_1001042',
    '11023_1001043',
    '11024_1001044',
    '11025_1001045',
    '11026_1001046',
    '11027_1001047',
    '11028_1001048',
    '11029_1001049',
    '11030_1001050',
    '11031_1001051',
    '11032_1001052',
    '11033_1001053',
    '11034_1001054',
    '11035_1001055',
    '11036_1001056',
    '11038_1001058',
    '11039_1001059',
    '11040_1001060',
    '11041_1001061',
    '11042_1001062',
    '11044_1001064',
    '11046_1001066',
    '11047_1001067',
    '11048_1001068',
    '11049_1001069',
    '11050_1001070',
    '11051_1001071',
    '11052_1001072',
    '11053_1001073',
    '11054_1001074',
    '11056_1001077',
    '11057_1001078',
    '11058_1001079',
    '11059_1001080',
    '11059_1001081',
    '11060_1001082',
    '11061_1001083',
    '11062_1001084',
    '11063_1001085',
    '11064_1001086',
    '11065_1001087',
    '11066_1001088',
    '11068_1001090',
    '11069_1001091',
    '11070_1001092',
    '11071_1001093',
    '11073_1001095',
    '11074_1001096',
    '11075_1001097',
    '11076_1001098',
    '11077_1001099',
    '11078_1001100',
    '11079_1001101',
    '11080_1001102',
    '11082_1001104',
    '11084_1001106',
    '11085_1001107',
    '11086_1001108',
    '11087_1001109',
    '11087_1001110',
    '11088_1001111',
    '11089_1001112',
    '11090_1001113',
    '11091_1001114',
    '11092_1001115',
    '11094_1001117',
    '11096_1001119',
    '11097_1001120',
    '11098_1001121',
    '11099_1001122',
    '11100_1001123',
    '11101_1001124',
    '11102_1001125',
    '11103_1001126',
    '11104_1001127',
    '11105_1001128',
    '11106_1001129',
    '11107_1001130',
    '11108_1001131',
    '11109_1001132',
    '11110_1001133',
    '11112_1001135',
    '11113_1001136',
    '11114_1001137',
    '11116_1001139',
    '11118_1001141',
    '11119_1001142',
    '11120_1001143',
    '11121_1001144',
    '11122_1001145',
    '11124_1001147',
    '11125_1001148',
    '11126_1001149',
    '11127_1001150',
    '11128_1001151',
    '11129_1001152',
    '11130_1001153',
    '11131_1001154',
    '11132_1001155',
    '11134_1001157',
    '11135_1001158',
    '11136_1001159',
    '11137_1001160',
    '11138_1001161',
    '11139_1001162',
    '11140_1001163',
    '11141_1001164',
    '11142_1001165',
    '11144_1001167',
    '11145_1001168',
    '11147_1001170',
    '11148_1001171',
    '11149_1001172',
    '11150_1001173',
    '11151_1001174',
    '11152_1001175',
    '11153_1001176',
    '11154_1001177',
    '11155_1001178',
    '11156_1001179',
    '11158_1001181',
    '11159_1001182',
    '11160_1001183',
    '11161_1001184',
    '11162_1001185',
    '11163_1001186',
    '11164_1001187',
    '11165_1001188',
    '11166_1001189',
    '11167_1001190',
    '11168_1001191',
    '11170_1001193',
    '11171_1001194',
    '11172_1001195',
    '11174_1001197',
    '11175_1001198',
    '11176_1001199',
    '11177_1001200',
    '11178_1001201',
    '11180_1001203',
    '11181_1001204',
    '11182_1001205',
    '11183_1001206',
    '11184_1001207',
    '11185_1001208',
    '11186_1001209',
    '11187_1001210',
    '11188_1001211',
    '11189_1001212',
    '11190_1001213',
    '11191_1001214',
    '11192_1001215',
    '11193_1001216',
    '11194_1001217',
    '11195_1001218',
    '11196_1001219',
    '11197_1001220',
    '11198_1001221',
    '11199_1001222',
    '11200_1001223',
    '11201_1001224',
    '11202_1001225',
    '11203_1001226',
    '11204_1001227',
    '11205_1001228',
    '11206_1001229',
    '11208_1001231',
    '11209_1001232',
    '11210_1001233',
    '11211_1001234',
    '11212_1001235',
    '11213_1001236',
    '11214_1001237',
    '11215_1001238',
    '11216_1001239',
    '11217_1001240',
    '11218_1001241',
    '11219_1001242',
    '11220_1001243',
    '11221_1001244',
    '11222_1001245',
    '11223_1001246',
    '11224_1001247',
    '11225_1001248',
    '11226_1001249',
    '11227_1001250',
    '11228_1001251',
    '11229_1001252',
    '11230_1001253',
    '11231_1001254',
    '11232_1001255',
    '11233_1001256',
    '11234_1001257',
    '11235_1001258',
    '11236_1001259',
    '11237_1001260',
    '11238_1001261',
    '11241_1001264',
    '11242_1001265',
    '11244_1001267',
    '11246_1001269',
    '11247_1001270',
    '11249_1001272',
    '11250_1001273',
    '11251_1001274',
    '11252_1001275',
    '11253_1001276',
    '11254_1001277',
    '11255_1001278',
    '11256_1001279',
    '11257_1001280',
    '11259_1001282',
    '11260_1001283',
    '11261_1001284',
    '11262_1001285',
    '11263_1001286',
    '11264_1001287',
    '11265_1001288',
    '11267_1001290',
    '11268_1001291',
    '11269_1001292',
    '11270_1001293',
    '11271_1001294',
    '11272_1001295',
    '11273_1001296',
    '11275_1001298',
    '11276_1001299',
    '11277_1001300',
    '11278_1001301',
    '11279_1001302',
    '11280_1001303',
    '11281_1001304',
    '11282_1001305',
    '11284_1001307',
    '11286_1001309',
    '11287_1001310',
    '11288_1001311',
    '11289_1001312',
    '11290_1001313',
    '11291_1001314',
    '11292_1001315',
    '11293_1001316',
    '11294_1001317',
    '11295_1001318',
    '11297_1001320',
    '11298_1001321',
    '11299_1001322',
    '11300_1001323',
    '11301_1001324',
    '11303_1001326',
    '11304_1001327',
    '11305_1001328',
    '11306_1001329',
    '11307_1001330',
    '11308_1001331',
    '11309_1001332',
    '11310_1001333',
    '11311_1001334',
    '11312_1001335',
    '11314_1001337',
    '11315_1001338',
    '11316_1001339',
    '11317_1001340',
    '11318_1001341',
    '11319_1001342',
    '11320_1001343',
    '11321_1001344',
    '11323_1001346',
    '11324_1001347',
    '11325_1001348',
    '11326_1001349',
    '11327_1001350',
    '11328_1001351',
    '11329_1001352',
    '11330_1001353',
    '11331_1001354',
    '11335_1001358',
    '11337_1001360',
    '11338_1001361',
    '11339_1001362',
    '11340_1001363',
    '11342_1001365',
    '11343_1001366',
    '11344_1001367',
    '11345_1001368',
    '11347_1001370',
    '11348_1001371',
    '11349_1001372',
    '11351_1001374',
    '11353_1001376',
    '11354_1001377',
    '11355_1001378',
    '11356_1001379',
    '11357_1001380',
    '11358_1001381',
    '11359_1001382',
    '11360_1001383',
    '11361_1001384',
    '11362_1001385',
    '11363_1001386',
    '11364_1001387',
    '11365_1001388',
    '11366_1001389',
    '11368_1001391',
    '11370_1001393',
    '11371_1001394',
    '11372_1001395',
    '11373_1001396',
    '11374_1001397',
    '11375_1001398',
    '11376_1001399',
    '11377_1001400',
    '11378_1001401',
    '11379_1001402',
    '11380_1001403',
    '11381_1001404',
    '11382_1001405',
    '11383_1001406',
    '11383_1001407',
    '11384_1001408',
    '11385_1001409',
    '11386_1001410',
    '11387_1001411',
    '11388_1001412',
    '11389_1001413',
    '11390_1001414',
    '11391_1001415',
    '11392_1001416',
    '11393_1001417',
    '11394_1001418',
    '11395_1001419',
    '11396_1001420',
    '11397_1001421',
    '11398_1001422',
    '11399_1001423',
    '11401_1001425',
    '11402_1001426',
    '11403_1001427',
    '11404_1001428',
    '11405_1001429',
    '11406_1001430',
    '11407_1001431',
    '11408_1001432',
    '11409_1001433',
    '11410_1001434',
    '11411_1001435',
    '11412_1001436',
    '11413_1001437',
    '11414_1001438',
    '11415_1001439',
    '11416_1001440',
    '11417_1001441',
    '11418_1001442',
    '11419_1001443',
    '11420_1001444',
    '11421_1001445',
    '11422_1001446',
    '11423_1001447',
    '11424_1001448',
    '11427_1001451',
    '11428_1001452',
    '11429_1001453',
    '11430_1001454',
    '11431_1001455',
    '11432_1001456',
    '11433_1001457',
    '11434_1001458',
    '11435_1001459',
    '11436_1001460',
    '11438_1001462',
    '11439_1001463',
    '11440_1001464',
    '11441_1001465',
    '11442_1001466',
    '11443_1001467',
    '11444_1001468',
    '11445_1001469',
    '11446_1001470',
    '11447_1001471',
    '11448_1001472',
    '11449_1001473',
    '11450_1001474',
    '11452_1001476',
    '11453_1001477',
    '11454_1001478',
    '11455_1001479',
    '11456_1001480',
    '11457_1001481',
    '11458_1001482',
    '11459_1001483',
    '11460_1001484',
    '11461_1001485',
    '11462_1001486',
    '11463_1001487',
    '11464_1001488',
    '11465_1001489',
    '11466_1001490',
    '11467_1001491',
    '11469_1001493',
    '11470_1001494',
    '11471_1001495',
    '11473_1001497',
    '11474_1001498',
    '11475_1001499'
]

__all__ = [
    "subject_list_annotated"
]
