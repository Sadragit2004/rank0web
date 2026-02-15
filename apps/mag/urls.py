from django.urls import path
from .views import MagAdsList,MagsViewAll,MagsViewBlogMain,show_meta_main,top_parent_groups_title,search_view,MagDetailView,ShowByGroup,top_parent_groups,main,show_slider,MagsView,show_best_Author,ExplorerMagView,group_list_view,MagTitleList


app_name = 'mag'

urlpatterns = [


    path('mag',main,name='index'),
    path('slider',show_slider,name='slider'),
    path('s/mags/',MagsView,name='mags'),
    path('s/authors-best/',show_best_Author,name='show-best-aut'),
    path('s/explorer/',ExplorerMagView,name='explorer'),
    path('s/top-parent/',top_parent_groups,name='top-group'),
    path('s/header-group/',group_list_view,name='groups_header'),
    path('mag/<str:slug>/', ShowByGroup.as_view(), name='show-mag'),  # مسیر مادر
    path('mag/<str:group_slug>/<str:slug>', MagDetailView.as_view(), name='show_detail_group'),
    path('s/search-mag/',search_view,name='search'),
    path('s/top_title_footer/',top_parent_groups_title,name='top_title'),
    path('s/mag-footer/',MagTitleList,name='top_title_mag'),
    path('show-meta/',show_meta_main,name='meta'),
    path('mags',MagsViewAll,name='MagsViewAll2'),
    path('s/MagsViewBlogMain/',MagsViewBlogMain,name='MagsViewBlogMain2'),
    path('s/MagAdsList/',MagAdsList,name='footerads')



]