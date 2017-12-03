from django.db import models

# Create your models here.
class UserName(models.Model):
    user_name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.user_name

class first_question(models.Model):
    question = models.ForeignKey(UserName)


########################################
class Comment(models.Model):
    comment = models.TextField(max_length = 1000)

    def __str__(self):
        return self.comment

class StarRate(models.Model):
    star_rate = models.TextField(max_length=1)
#아래는 참고코드(this is reference code)
#     $('#click').raty({
#   click: function(score, evt) {
#     alert('ID: ' + this.attr('id') + '\nscore: ' + score + '\nevent: ' + evt);
#   }
# });
#
# <div id="click"></div>
#https://www.alpinestyle.co.il/media/vendor/jquery.raty-1.4.3/