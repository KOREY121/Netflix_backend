from django.db import models

class Device(models.Model):

    class DeviceType(models.TextChoices):
        MOBILE = 'mobile', 'Mobile'
        WEB = 'web', 'Web'
        TV = 'TV', 'Smart TV'
        TABET = 'tabet', 'Tablet'
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='devices') 
    device_name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100, choices= DeviceType.choices)
    last_active_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'devices'

    def __str__(self):
        return f'{self.user.email} - {self.device_name}'
    

class StreamingSession(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        ENDED = 'ended', 'Ended'

    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE)
    device = models.ForeignKey( Device, on_delete=models.CASCADE)
    content = models.ForeignKey('content.Content', on_delete=models.CASCADE)
    episode = models.ForeignKey('content.Episode', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank= True)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        db_table = 'streaming_sessions'

    def __str__(self):
        return f'{self.profile.name} = {self.status}'
    
class WatchHistory(models.Model):
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='watch_history')
    content = models.ForeignKey('content.Content', on_delete=models.CASCADE)
    episode = models.ForeignKey('content.Episode', on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now=True)
    progress = models.PositiveSmallIntegerField(default=0, help_text='0-100%')
    
    class Meta:
        db_table = 'watch_history'

    def __str__(self):
        return f'{self.profile.name} -{self.progress}%'
    
class Download(models.Model):
    profile = models.ForeignKey('profiles.Profile', on_delete= models.CASCADE,related_name='downloads')
    content = models.ForeignKey('content.Content', on_delete= models.CASCADE, null=True, blank=True)
    episode = models.ForeignKey('content.Episode' , on_delete= models.CASCADE,null=True, blank=True)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        db_table = 'downloads'
    def __str__(self):
        return f'{self.profile.name} download'
    
    
class SearchHistory(models.Model):
    profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='search_history')
    query_text = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table ='search_history'

    def __str__(self):
        return f'{self.profile.name} → "{self.query_text}"'

    