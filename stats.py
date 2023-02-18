import cbsodata

table_id = '85058NED'
year = 2015
province = 'PV25  '

ds = cbsodata.get_data(
      table_id=table_id,
      filters="Perioden gt '" + str(year) + "JJ00' " 
              "and SoortBewoondeWoonruimten eq 'A050218' "
              "and RegioS eq '" + province + "'",
      select='SoortBewoondeWoonruimten, '
             'Perioden, '
             'BewoondeWoonruimte_1, '
             'RegioS'
)
print(ds)
