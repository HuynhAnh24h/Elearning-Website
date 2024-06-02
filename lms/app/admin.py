from django.contrib import admin

from .models import Categories
from .models import Author
from .models import Course
from .models import Level
from .models import Will_Learn
from .models import Requirements
from .models import Lesson
from .models import Video
from .models import UserCourse
# Thêm danh sách khoá kỹ năng trong khoá học
class Will_Learn_TabularInline(admin.TabularInline):
    model = Will_Learn

# Thêm danh sách yêu cầu trước khoá học
class RequirementsTabularInline(admin.TabularInline):
    model = Requirements

# Thêm danh sách bài học
class VideoTabularInline(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines = (Will_Learn_TabularInline,RequirementsTabularInline, VideoTabularInline)


# Register your models here.
admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course, course_admin)
admin.site.register(Level)
admin.site.register(Will_Learn)
admin.site.register(Requirements)
admin.site.register(Lesson)
admin.site.register(Video)


admin.site.register(UserCourse)