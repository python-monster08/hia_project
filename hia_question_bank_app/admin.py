from django.contrib import admin
from .models import QuestionBank

class QuestionBankAdmin(admin.ModelAdmin):
    # Define the fields to be displayed in the list view
    list_display = (
        'question_number', 'type_of_question', 'question_sub_type', 'exam_name', 'exam_stage', 'exam_year', 
        'subject_name', 'area_name', 'part_name', 'marks', 'negative_marks', 'degree_of_difficulty'
    )

    # Define the fields that can be used to filter the list
    list_filter = (
        'exam_name', 'exam_stage', 'exam_year', 'subject_name', 
        'area_name', 'degree_of_difficulty', 'language'
    )

    # Define the fields that will be searchable
    search_fields = (
        'question_number', 'type_of_question', 'exam_name', 'subject_name', 
        'area_name', 'part_name', 'degree_of_difficulty', 'question_part'
    )

    # Define the fieldsets to organize fields in the detail view
    fieldsets = (
        (None, {
            'fields': (
                'question_number', 'type_of_question', 'exam_name', 'exam_stage', 'exam_year', 
                'language', 'script', 'marks', 'negative_marks', 'degree_of_difficulty', 'question_sub_type'
            )
        }),
        ('Question Details', {
            'fields': (
                'question_part', 'question_part_first_part', 'list_1_name', 'list_2_name', 
                'list_1_row1', 'list_2_row1', 'list_1_row2', 'list_2_row2', 'list_1_row3', 
                'list_2_row3', 'list_1_row4', 'list_2_row4', 'list_1_row5', 'list_2_row5', 
                'list_1_row6', 'list_2_row6', 'list_1_row7', 'list_2_row7', 'list_1_row8', 
                'list_2_row8', 'list_1_row9', 'list_2_row9', 'question_part_third_part'
            )
        }),
        ('Objective Fields', {
            'fields': ('answer_option_a', 'answer_option_b', 'answer_option_c', 'answer_option_d')
        }),
        ('Correct Answer', {
            'fields': ('correct_answer_choice', 'correct_answer_description')
        }),
        ('Extra Information', {
            'fields': ('image', 'subject_name', 'area_name', 'part_name')
        }),
        ('Table Headers', {
            'fields': ('table_head_a', 'table_head_b', 'table_head_c', 'table_head_d')
        }),
        ('Table Data', {
            'fields': (
                'head_a_data1', 'head_a_data2', 'head_a_data3', 'head_a_data4',
                'head_b_data1', 'head_b_data2', 'head_b_data3', 'head_b_data4',
                'head_c_data1', 'head_c_data2', 'head_c_data3', 'head_c_data4',
                'head_d_data1', 'head_d_data2', 'head_d_data3', 'head_d_data4'
            )
        }),
    )

admin.site.register(QuestionBank, QuestionBankAdmin)
