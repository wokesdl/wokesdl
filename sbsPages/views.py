from django.shortcuts import render,redirect
from django.views import View
import smtplib
from email.mime.text import MIMEText
from django.contrib import messages


# This is the sounds by sdl home page
class SbsHome(View):
    def get(self,request):
        return render(request,'sbsPages/home.html')
    
class ArtistPage(View):
    def get(self,request):
        return render(request,'sbsPages/artistsPage.html')
    

class Kwelit(View):
    def get(self,request):
        return render(request,'sbsPages/kwelit.html')

class Santana(View):
    def get(self,request):
        return render(request,'sbsPages/santana.html')
    
    def post(self,request):
        if "sendMessage" in request.POST:
            message_text = request.POST.get("message", "").strip()

            if not message_text:
                messages.error(request, "Please enter a message before sending.")
                return redirect('/santana/')

            # Prepare the email
            msg = MIMEText(message_text)
            msg["Subject"] = "Message from fan!!!"
            msg["From"] = "info@longlivesdl.com"
            msg["To"] = " javangaiya253@gmail.com"

            try:
                # Send via Zoho SMTP SSL
                with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
                    server.login("info@longlivesdl.com", "gyn46qqStugX")
                    server.sendmail(msg["From"], msg["To"], msg.as_string())

                messages.success(request, "Your message has been sent to Javan Santana!")
            except Exception as e:
                # Log e if you want
                messages.error(request, f"Failed to send message: {e}")

        # in all cases, go back to the same page
        return redirect('/santana/')



class Montana(View):
    def get(self,request):
        return render(request,'sbsPages/montana.html')
    def post(self,request):
        if "sendMessage" in request.POST:
            message_text = request.POST.get("message", "").strip()

            if not message_text:
                messages.error(request, "Please enter a message before sending.")
                return redirect('/montana/')

            # Prepare the email
            msg = MIMEText(message_text)
            msg["Subject"] = "Message from fan!!!"
            msg["From"] = "info@longlivesdl.com"
            msg["To"] = "montannaa747@gmail"

            try:
                # Send via Zoho SMTP SSL
                with smtplib.SMTP_SSL("smtp.zoho.com", 465) as server:
                    server.login("info@longlivesdl.com", "gyn46qqStugX")
                    server.sendmail(msg["From"], msg["To"], msg.as_string())

                messages.success(request, "Your message has been sent to Danny Montanna!")
            except Exception as e:
                # Log e if you want
                messages.error(request, f"Failed to send message: {e}")

        # in all cases, go back to the same page
        return redirect('/montana/')

class Videos(View):
    def get(self,request):
        return render(request,'sbsPages/videos.html')

class Music(View):
    def get(self,request):
        return render(request,'sbsPages/music.html')