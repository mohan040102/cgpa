from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mech/',views.mech,name='mech'),
    path('mech/mech1/',views.mech1,name='mech1'),
    path('mech/mech1/result/',views.result,name='result'),
    path('mech/mech2/',views.mech2,name='mech2'),
    path('mech/mech2/result2/',views.result2,name='result2'),
    path('mech/mech3/',views.mech3,name='mech3'),
    path('mech/mech3/result3/',views.result3,name='result3'),
    path('mech/mech4/',views.mech4,name='mech4'),
    path('mech/mech4/result4/',views.result4,name='result4'),
    path('mech/mech5/',views.mech5,name='mech5'),
    path('mech/mech5/result5/',views.result5,name='result5'),
    path('mech/mech6/',views.mech6,name='mech6'),
    path('mech/mech6/result6/',views.result6,name='result6'),
    path('mech/mech7/',views.mech7,name='mech7'),
    path('mech/mech7/result7/',views.result7,name='result7'),
    path('mech/mech8/',views.mech8,name='mech8'),
    path('mech/mech8/result8/',views.result8,name='result8'),
    path('civil/',views.civil,name='civil'),
    path('civil/civil1/',views.civil1,name='civil1'),
    path('civil/civil1/result/',views.result,name='result'),
    path('civil/civil2/',views.civil2,name='civil2'),
    path('civil/civil2/result2/',views.result2,name='result2'),
    path('civil/civil3/',views.civil3,name='civil3'),
    path('civil/civil3/result3/',views.result3,name='result3'),
    path('civil/civil4/',views.civil4,name='civil4'),
    path('civil/civil4/result4/',views.result4,name='result4'),
    path('civil/civil5/',views.civil5,name='civil5'),
    path('civil/civil5/result5/',views.result5,name='result5'),
    path('civil/civil6/',views.civil6,name='civil6'),
    path('civil/civil6/result6',views.result6,name='result6'),
    path('civil/civil7/',views.civil7,name='civil7'),
    path('civil/civil7/result7/',views.result7,name='result7'),
    path('civil/civil8/',views.civil8,name='civil8'),
    path('civil/civil8/result8/',views.result8,name='result8'),
    path('am/',views.am,name='am'),
    path('am/am1/',views.am1,name='am'),
    path('am/am1/result',views.result,name='result'),
    path('am/am2/',views.am2,name="am2"),
    path('am/am2/result2/',views.result2,name='result'),
    path('am/am3/',views.am3,name='am3'),
    path('am/am3/result3',views.result3,name='result3'),
    path('am/am4/',views.am4,name='am4'),
    path('am/am4/result4',views.result4,name='result4'),
    path('am/am5/',views.am5,name='am5'),
    path('am/am5/result5',views.result5,name='result5'),
    path('am/am6/',views.am6,name='am6'),
    path('am/am6/result6',views.result6,name='result6'),
    path('am/am7/',views.am7,name='am7'),
    path('am/am7/result7/',views.result7,name='result7'),
    path('am/am8/',views.am8,name='am8'),
    path('am/am8/result8/',views.result8,name='result8'),
    path('eee/',views.eee,name='eee'),
    path('eee/eee1/',views.eee1,name='eee1'),
    path('eee/eee1/result',views.result,name='result'),
    path('eee/eee2/',views.eee2,name='eee2'),
    path('eee/eee2/result2/',views.result2,name='result2'),
    path('eee/eee3/',views.eee3,name='eee3'),
    path('eee/eee3/result3/',views.result3,name='result3'),
    path('eee/eee4/',views.eee4,name='eee4'),
    path('eee/eee4/result4/',views.result4,name='result4'),
    path('eee/eee5/',views.eee5,name='eee5'),
    path('eee/eee5/result5',views.result5,name='reult5'),
    path('eee/eee6/',views.eee6,name='eee6'),
    path('eee/eee6/result6',views.result6,name='result6'),
    path('eee/eee7/',views.eee7,name='eee7'),
    path('eee/eee7/result7',views.result7,name='result7'),
    path('eee/eee8/',views.eee8,name='eee8'),
    path('eee/eee8/result8/',views.result8,name='result8'),
    path('cse/',views.cse,name='cse'),
    path('cse/cse1/',views.cse1,name='cse1'),
    path('cse/cse1/result/',views.result,name='result'),
    path('cse/cse2/',views.cse2,name='cse2'),
    path('cse/cse2/result2/',views.result2,name='result2'),
    path('cse/cse3/',views.cse3,name='cse3'),
    path('cse/cse3/result3/',views.result3,name='result3'),
    path('cse/cse4/',views.cse4,name='cse4'),
    path('cse/cse4/result4/',views.result4,name='result4'),
    path('cse/cse5/',views.cse5,name='cse5'),
    path('cse/cse5/result5',views.result5,name='result5'),
    path('cse/cse6/',views.cse6,name='cse6'),
    path('cse/cse6/result6/',views.result6,name='result6'),
    path('cse/cse7/',views.cse7,name='cse7'),
    path('cse/cse7/result7/',views.result7,name='result7'),
    path('cse/cse8/',views.cse8,name='cse8'),
    path('ece/',views.ece,name='ece'),
    path('ece/ece1/',views.ece1,name='ece1'),
    path('ece/ece1/result',views.result,name='result'),
    path('ece/ece2/',views.ece2,name='ece2'),
    path('ece/ece2/result2/',views.result2,name='result2'),
    path('ece/ece3/',views.ece3,name='ece3'),
    path('ece/ece3/result3/',views.result3,name='result3'),
    path('ece/ece4/',views.ece4,name='ece4'),
    path('ece/ece4/result4',views.result4,name='result4'),
    path('ece/ece5/',views.ece5,name='ece5'),
    path('ece/ece5/result5/',views.result5,name='result5'),
    path('ece/ece6/',views.ece6,name='ece6'),
    path('ece/ece6/result6',views.result6,name='result6'),
    path('ece/ece7/',views.ece7,name='ece7'),
    path('ece/ece7/result7/',views.result7,name='result7'),
    path('ece/ece8/',views.ece8,name='ece8'),
    path('ece/ece8/result8/',views.result8,name='result8'),
    path('it/',views.it,name='it'),
    path('it/it1/',views.it1,name='it1'),
    path('it/it1/result/',views.result,name='result1'),
    path('it/it2/',views.it2,name='it2'),
    path('it/it2/result2/',views.result2,name='result2'),
    path('it/it3/',views.it3,name='it3'),
    path('it/it3/result3/',views.result3,name='result3'),
    path('it/it4/',views.it4,name='it4'),
    path('it/it4/result4/',views.result4,name='result4'),
    path('it/it5/',views.it5,name='it5'),
    path('it/it5/result5/',views.result5,name='result5'),
    path('it/it6/',views.it6,name='it6'),
    path('it/it6/result6/',views.result6,name='result6'),
    path('it/it7/',views.it7,name='it7'),
    path('it/it7/result7/',views.result7,name='result7'),
    path('it/it8/',views.it8,name='it8'),
    path('it/it8/result8/',views.result8,name='result8'),
    path('pro/',views.pro,name='pro'),
    path('pro/pro1/',views.pro1,name='pro1'),
    path('pro/pro1/result/',views.result,name='result'),
    path('pro/pro2/',views.pro2,name='pro2'),
    path('pro/pro2/result2/',views.result2,name='result2'),
    path('pro/pro3/',views.pro3,name='pro3'),
    path('pro/pro3/result3/',views.result3,name='result3'),
    path('pro/pro4/',views.pro4,name='pro4'),
    path('pro/pro4/result4/',views.result4,name='result4'),
    path('pro/pro5/',views.pro5,name='pro5'),
    path('pro/pro5/result5/',views.result5,name='result5'),
    path('pro/pro6/',views.pro6,name='pro6'),
    path('pro/pro6/result6/',views.result6,name='resul6'),
    path('pro/pro7/',views.pro7,name='pro7'),
    path('pro/pro7/result7/',views.result7,name='result7'),
    path('pro/pro8/',views.pro8,name='pro8'),
    path('pro/pro8/result8/',views.result8,name='result8'),
    path('btech/',views.btech,name='btech'),
    path('btech/btech1/',views.btech1,name='btech1'),
    path('btech/btech1/result/',views.result,name='result'),
    path('btech/btech2/',views.btech2,name='btech2'),
    path('btech/btech2/result2/',views.result2,name='result2'),
    path('btech/btech3/',views.btech3,name='btech3'),
    path('btech/btech3/result3/',views.result3,name='result3'),
    path('btech/btech4/',views.btech4,name='btech4'),
    path('btech/btech4/result4/',views.result4,name='result4'),
    path('btech/btech5/',views.btech5,name='btech'),
    path('btech/btech5/result5/',views.result5,name='result5'),
    path('btech/btech6/',views.btech6,name='btech6'),
    path('btech/btech6/result6/',views.result6,name='result6'),
    path('btech/btech7/',views.btech7,name='btech7'),
    path('btech/btech7/result7/',views.result7,name='result7'),
    path('btech/btech8/',views.btech8,name='btech8'),
    path('btech/btech8/result8/',views.result8,name='result8'),
    path('food/',views.food,name='food'),
    path('food/food1/',views.food1,name='food1'),
    path('food/food1/result/',views.result,name='result'),
    path('food/food2/',views.food2,name='food'),
    path('food/food2/result2/',views.result2,name='result2'),
    path('food/food3/',views.food3,name='food3'),
    path('food/food3/result3/',views.result3,name='result3'),
    path('food/food4/',views.food4,name='food4'),
    path('food/food4/result4/',views.result4,name='result4'),
    path('food/food5/',views.food5,name='food5'),
    path('food/food5/result5/',views.result5,name='result5'),
    path('food/food6/',views.food6,name='food6'),
    path('food/food6/result6',views.result6,name='result6'),
    path('food/food7/',views.food7,name='food7'),
    path('food/food7/result7/',views.result7,name='result7'),
    path('food/food8/',views.food8,name='food8'),
    path('food/food8/result8/',views.result8,name='result8'),
    path('chem/',views.chem,name='chem'),
    path('chem/chem1/',views.chem1,name='chem1'),
    path('chem/chem1/result/',views.result,name='result'),
    path('chem/chem2/',views.chem2,name='chem2'),
    path('chem/chem2/result2',views.result2,name='result2'),
    path('chem/chem3/',views.chem3,name='chem3'),
    path('chem/chem3/result3/',views.result3,name='result3'),
    path('chem/chem4/',views.chem4,name='chem4'),
    path('chem/chem4/result4/',views.result4,name='result4'),
    path('chem/chem5/',views.chem5,name='chem5'),
    path('chem/chem5/result5/',views.result5,name='result5'),
    path('chem/chem6/',views.chem6,name='chem6'),
    path('chem/chem6/result6/',views.result6,name='result6'),
    path('chem/chem7/',views.chem7,name='chem7'),
    path('chem/chem7/result7/',views.result7,name='result7'),
    path('chem/chem8/',views.chem8,name='chem8'),
    path('chem/chem8/result8/',views.result8,name='result8')
]
