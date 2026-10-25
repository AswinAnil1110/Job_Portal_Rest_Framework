from rest_framework import serializers
from JobApp.models import JobDb,ApplicationDb

class JobSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=100)
    location = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=100)
    job_type = serializers.ChoiceField(choices=JobDb.job_type_choices)
    experience_level = serializers.ChoiceField(choices=JobDb.experience_choices)
    salary = serializers.IntegerField()
    department = serializers.CharField(max_length=100)
    is_active = serializers.BooleanField(default=True)
    published_date = serializers.DateTimeField(read_only=True)

class ApplicationSerializer(serializers.Serializer):
    applicant_name = serializers.CharField(max_length=100)
    applicant_email = serializers.EmailField()
    job = serializers.IntegerField()
    qualification = serializers.CharField(max_length=100)
    experience_years = serializers.IntegerField()
    status = serializers.ChoiceField(choices=ApplicationDb.status_choices,default='pending',read_only=True)
    application_date = serializers.DateTimeField(read_only=True)

    def validate_job(self,value):
        if not JobDb.objects.filter(id=value).exists():
            raise serializers.ValidationError("Job Does Not Exist....!")
        return value