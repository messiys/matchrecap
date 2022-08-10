# Generated by Django 4.0.4 on 2022-06-29 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='分类名称')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='分类描述')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='Sidebar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='模块名称')),
                ('display_type', models.PositiveIntegerField(choices=[(1, '搜索'), (2, '最新文章'), (3, '最热文章'), (4, '最近评论'), (5, '文章归档'), (6, 'HTML')], default=1, verbose_name='展示类型')),
                ('content', models.CharField(blank=True, default='', help_text='如果设置的不是HTML类型，可为空', max_length=500, verbose_name='内容')),
                ('sort', models.PositiveIntegerField(default=1, help_text='序号越大越靠前', verbose_name='排序')),
                ('status', models.PositiveIntegerField(choices=[(1, '隐藏'), (2, '展示')], default=2, verbose_name='状态')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '侧边栏',
                'verbose_name_plural': '侧边栏',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='文章标签')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=61, verbose_name='文章标题')),
                ('desc', models.TextField(blank=True, default='', max_length=200, verbose_name='文章描述')),
                ('content', models.TextField(verbose_name='文章详情')),
                ('is_hot', models.BooleanField(default=False, verbose_name='是否热门')),
                ('pv', models.IntegerField(default=0, verbose_name='浏览量')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='分类')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('tags', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.tag', verbose_name='文章标签')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
    ]
