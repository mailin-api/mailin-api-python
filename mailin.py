import httplib2
import json
import datetime
import hmac 
from hashlib import sha1,md5
import base64

class Mailin:
  """ This is the Mailin client class
  """
  def __init__(self,base_url,access_key,secret_key):
    self.base_url = base_url
    self.access_key = access_key
    self.secret_key = secret_key     
  def do_request(self,resource,method,indata): 
    url = self.base_url + "/" + resource
    h = httplib2.Http(".cache")
    # Authorization header 
    content_type = "application/json"
    md5_content = ""
    if indata!="":
      md5_content = md5(indata).hexdigest()
    c_date_time = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
    sign_string = method+"\n"+md5_content+"\n"+content_type+"\n"+c_date_time+"\n"+url
    hashed = hmac.new(self.secret_key,sign_string.encode('utf8'),sha1)
    signature = base64.b64encode(hashed.hexdigest())
    r,c = h.request(url,method,body=indata,headers={'X-mailin-date':c_date_time,'content-type':content_type,'Authorization':self.access_key+":"+signature})    
    return json.loads(c)  
  def get(self,resource,indata):
    return self.do_request(resource,"GET",indata)
  def post(self,resource,indata):
    return self.do_request(resource,"POST",indata)
  def put(self,resource,indata):
    return self.do_request(resource,"PUT",indata)
  def delete(self,resource,indata):
    return self.do_request(resource,"DELETE",indata)
  def get_account(self,):
    return self.get("account","")
  def send_sms(self,to,from_name,text,web_url,tag):
    return self.post("sms",json.dumps({"text":text,"tag":tag,"web_url":web_url,"from":from_name,"to":to}))
  def get_campaigns(self,type):
   if type == "":
   	return self.get("campaign/","")
   else:
   	return self.get("campaign/type/" + type + "/","")
  def get_campaign(self,id):
    return self.get("campaign/" + id,"")
  def create_campaign(self,category,from_name,name,bat_sent,html_content,html_url,listid,scheduled_date,subject,from_email,reply_to,exclude_list):
    return self.post("campaign",json.dumps({"category":category,"from_name":from_name,"name":name,"bat_sent":bat_sent,"html_content":html_content,"html_url":html_url,"listid":listid,"scheduled_date":scheduled_date,"subject":subject,"from_email":from_email,"reply_to":reply_to,"exclude_list":exclude_list}))
  def delete_campaign(self,id):
    return self.delete("campaign/" + id,"")
  def update_campaign(self,id,category,from_name,name,bat_sent,html_content,html_url,listid,scheduled_date,subject,from_email,reply_to,exclude_list):
    return self.put("campaign/" + id,json.dumps({"category":category,"from_name":from_name,"name":name,"bat_sent":bat_sent,"html_content":html_content,"html_url":html_url,"listid":listid,"scheduled_date":scheduled_date,"subject":subject,"from_email":from_email,"reply_to":reply_to,"exclude_list":exclude_list}))
  def campaign_report_email(self,id,lang,email_subject,email_to,email_content_type,email_bcc,email_cc,email_body):
    return self.post("campaign/" + id + "/report",json.dumps({"lang":lang,"email_subject":email_subject,"email_to":email_to,"email_content_type":email_content_type,"email_bcc":email_bcc,"email_cc":email_cc,"email_body":email_body}))
  def campaign_recipients_export(self,id,notify_url,type):
    return self.post("campaign/" + id + "/report",json.dumps({"notify_url":notify_url,"type":type}))
  def get_processes(self,):
    return self.get("process","")
  def get_process(self,id):
    return self.get("process/" + id,"")
  def get_lists(self,):
    return self.get("list","")
  def get_list(self,id):
    return self.get("list/" + id,"")
  def create_list(self,list_name,list_parent):
    return self.post("list",json.dumps({"list_name":list_name,"list_parent":list_parent}))
  def delete_list(self,id):
    return self.delete("list/" + id,"")
  def update_list(self,id,list_name,list_parent):
    return self.put("list/" + id,json.dumps({"list_name":list_name,"list_parent":list_parent}))
  def add_users_list(self,id,users):
    return self.post("list/" + id + "/users",json.dumps({"users":users}))
  def delete_users_list(self,id,users):
    return self.delete("list/" + id + "/delusers",json.dumps({"users":users}))
  def send_email(self,to,subject,from_name,html,text,cc,bcc,replyto,attachment,headers):
    return self.post("email",json.dumps({"cc":cc,"text":text,"bcc":bcc,"replyto":replyto,"html":html,"to":to,"attachment":attachment,"from":from_name,"subject":subject,"headers":headers}))
  def get_webhooks(self,):
    return self.get("webhook","")
  def get_webhook(self,id):
    return self.get("webhook/" + id,"")
  def create_webhook(self,url,description,events):
    return self.post("webhook",json.dumps({"url":url,"description":description,"events":events}))
  def delete_webhook(self,id):
    return self.delete("webhook/" + id,"")
  def update_webhook(self,id,url,description,events):
    return self.put("webhook/" + id,json.dumps({"url":url,"description":description,"events":events}))
  def get_statistics(self,aggregate,tag,days,end_date,start_date):
    return self.post("statistics",json.dumps({"aggregate":aggregate,"tag":tag,"days":days,"end_date":end_date,"start_date":start_date}))
  def get_user(self,id):
    return self.get("user/" + id,"")
  def get_user_stats(self,id,t):
    return self.get("user/" + id + "/" + t,"")
  def create_user(self,attributes,blacklisted,email,listid):
    return self.post("user",json.dumps({"attributes":attributes,"blacklisted":blacklisted,"email":email,"listid":listid}))
  def delete_user(self,id):
    return self.delete("user/" + id,"")
  def update_user(self,id,attributes,blacklisted,listid,listid_unlink):
    return self.put("user/" + id,json.dumps({"attributes":attributes,"blacklisted":blacklisted,"listid":listid,"listid_unlink":listid_unlink}))
  def import_users(self,url,listids,notify_url,name):
    return self.post("user/import",json.dumps({"url":url,"listids":listids,"notify_url":notify_url,"name":name}))
  def export_users(self,export_attrib,filer,notify_url):
    return self.post("user/export",json.dumps({"export_attrib":export_attrib,"filer":filer,"notify_url":notify_url}))
  def get_attributes(self,):
    return self.get("attribute","")
  def get_attribute(self,id):
    return self.get("attribute/" + id,"")
  def create_attribute(self,type,data):
    return self.post("attribute",json.dumps({"type":type,"data":data}))
  def delete_attribute(self,id,data):
    return self.post("attribute/" + id,json.dumps({"data":data}))
  def get_report(self,limit,start_date,end_date,offset,date,days,email):
    return self.post("report",json.dumps({"limit":limit,"start_date":start_date,"end_date":end_date,"offset":offset,"date":date,"days":days,"email":email}))
  def get_folders(self,):
    return self.get("folder","")
  def get_folder(self,id):
    return self.get("folder/" + id,"")
  def create_folder(self,name):
    return self.post("folder",json.dumps({"name":name}))
  def delete_folder(self,id):
    return self.delete("folder/" + id,"")
  def update_folder(self,id,name):
    return self.put("folder/" + id,json.dumps({"name":name}))
  def delete_bounces(self,start_date,end_date,email):
    return self.post("bounces",json.dumps({"start_date":start_date,"end_date":end_date,"email":email}))

