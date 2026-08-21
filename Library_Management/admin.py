from django.contrib import admin

from Library_Management.models import Bookdetails, Categories, Publisher, Books, Author


# Register your models here.
class Bookdetailsadmin(admin.ModelAdmin):
     list_display = ( 'id','isbn','pages','language','created_at','updated_at' )
     search_fields = ('isbn','pages','language','created_at','updated_at' )
admin.site.register(Bookdetails, Bookdetailsadmin)

class Categoriesadmin(admin.ModelAdmin):
    list_display = ( 'id','category_name','created_at','updated_at' )
    search_fields = ('category_name','created_at','updated_at' )
admin.site.register(Categories, Categoriesadmin)

class Publisheradmin(admin.ModelAdmin):
    list_display = ( 'id','publisher_name','created_at','updated_at' )
    search_fields = ('publisher_name','created_at','updated_at' )
admin.site.register(Publisher, Publisheradmin)

class Booksadmin(admin.ModelAdmin):
    list_display = ( 'id','title','created_at','updated_at' )
    search_fields = ('title','created_at','updated_at' )
admin.site.register(Books, Booksadmin)

class Authoradmin(admin.ModelAdmin):
    list_display = ( 'id','name','created_at','updated_at' )
    search_fields = ('name','created_at','updated_at' )
admin.site.register(Author, Authoradmin)

