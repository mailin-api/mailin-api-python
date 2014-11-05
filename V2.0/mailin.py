import httplib2
import json

class Mailin:
  """ This is the Mailin client class
  """
  def __init__(self,base_url,api_key):
    self.base_url = base_url
    self.api_key = api_key
  def do_request(self,resource,method,indata): 
    url = self.base_url + "/" + resource
    h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
    content_type = "application/json"
    r,c = h.request(url,method,body=indata,headers={'api-key':self.api_key, 'content-type':content_type})   
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
  def get_smtp_details(self,):
    return self.get("account/smtpdetail","")
  def create_child_account(self,email,password,company_org,first_name,last_name,credits):
    return self.post("account",json.dumps({"child_email":email,"password":password,"company_org":company_org,"first_name":first_name,"last_name":last_name,"credits":credits}))
  def update_child_account(self,child_authkey,company_org,first_name,last_name,password):
    return self.put("account",json.dumps({"auth_key":child_authkey,"company_org":company_org,"first_name":first_name,"last_name":last_name,"password":password}))
  def delete_child_account(self,child_authkey):
    return self.delete("account/" + child_authkey,"")
  def get_reseller_child(self,child_authkey):
    return self.post("account/getchildv2",json.dumps({"auth_key":child_authkey}))
  def add_remove_child_credits(self,child_authkey,add_credits,remove_credits):
    return self.post("account/addrmvcredit",json.dumps({"auth_key":child_authkey,"add_credit":add_credits,"rmv_credit":remove_credits}))
  def send_sms(self,to,from_name,text,web_url,tag,type):
    return self.post("sms",json.dumps({"text":text,"tag":tag,"web_url":web_url,"from":from_name,"to":to,"type":type}))
  def create_sms_campaign(self,camp_name,sender,content,bat_sent,listids,exclude_list,scheduled_date):
    return self.post("sms",json.dumps({"name":camp_name,"sender":sender,"content":content,"bat":bat_sent,"listid":listids,"exclude_list":exclude_list,"scheduled_date":scheduled_date}))
  def update_sms_campaign(self,id,camp_name,sender,content,bat_sent,listids,exclude_list,scheduled_date):
    return self.put("sms/" + id,json.dumps({"name":camp_name,"sender":sender,"content":content,"bat":bat_sent,"listid":listids,"exclude_list":exclude_list,"scheduled_date":scheduled_date}))
  def send_bat_sms(self,campid,mobilephone):
    return self.get("sms/" + campid,json.dumps({"to":mobilephone}))
  def get_campaigns_v2(self,type,status,page,page_limit):
   if type == "" and status == "" and page == "" and page_limit == "":
    return self.get("campaign/detailsv2/","")
   else:
    return self.get("campaign/detailsv2/type/" + type + "/status/" + status + "/page/" + page + "/page_limit/" + page_limit + "/","")
  def get_campaign_v2(self,id):
    return self.get("campaign/" + id + "/detailsv2/","")
  def create_campaign(self,category,from_name,name,bat_sent,html_content,html_url,listid,scheduled_date,subject,from_email,reply_to,to_field,exclude_list):
    return self.post("campaign",json.dumps({"category":category,"from_name":from_name,"name":name,"bat_sent":bat_sent,"html_content":html_content,"html_url":html_url,"listid":listid,"scheduled_date":scheduled_date,"subject":subject,"from_email":from_email,"reply_to":reply_to,"to_field":to_field,"exclude_list":exclude_list}))
  def delete_campaign(self,id):
    return self.delete("campaign/" + id,"")
  def update_campaign(self,id,category,from_name,name,bat_sent,html_content,html_url,listid,scheduled_date,subject,from_email,reply_to,to_field,exclude_list):
    return self.put("campaign/" + id,json.dumps({"category":category,"from_name":from_name,"name":name,"bat_sent":bat_sent,"html_content":html_content,"html_url":html_url,"listid":listid,"scheduled_date":scheduled_date,"subject":subject,"from_email":from_email,"reply_to":reply_to,"to_field":to_field,"exclude_list":exclude_list}))
  def campaign_report_email(self,id,lang,email_subject,email_to,email_content_type,email_bcc,email_cc,email_body):
    return self.post("campaign/" + id + "/report",json.dumps({"lang":lang,"email_subject":email_subject,"email_to":email_to,"email_content_type":email_content_type,"email_bcc":email_bcc,"email_cc":email_cc,"email_body":email_body}))
  def campaign_recipients_export(self,id,notify_url,type):
    return self.post("campaign/" + id + "/recipients",json.dumps({"notify_url":notify_url,"type":type}))
  def send_bat_email(self,campid,email_to):
    return self.post("campaign/" + campid + "/test",json.dumps({"emails":email_to}))
  def create_trigger_campaign(self,category,from_name,name,bat_sent,html_content,html_url,listid,scheduled_date,subject,from_email,reply_to,to_field,exclude_list,recurring):
    return self.post("campaign",json.dumps({"category":category,"from_name":from_name,"trigger_name":name,"bat":bat_sent,"html_content":html_content,"html_url":html_url,"listid":listid,"scheduled_date":scheduled_date,"subject":subject,"from_email":from_email,"reply_to":reply_to,"to_field":to_field,"exclude_list":exclude_list,"recurring":recurring}))
  def update_trigger_campaign(self,id,category,from_name,name,bat_sent,html_content,html_url,listid,scheduled_date,subject,from_email,reply_to,to_field,exclude_list,recurring):
    return self.put("campaign/" + id,json.dumps({"category":category,"from_name":from_name,"trigger_name":name,"bat":bat_sent,"html_content":html_content,"html_url":html_url,"listid":listid,"scheduled_date":scheduled_date,"subject":subject,"from_email":from_email,"reply_to":reply_to,"to_field":to_field,"exclude_list":exclude_list,"recurring":recurring}))
  def share_campaign(self,campaign_ids):
    return self.post("campaign/sharelinkv2",json.dumps({"camp_ids":campaign_ids}))
  def update_campaign_status(self,id,status):
    return self.put("campaign/" + id + "/updatecampstatus",json.dumps({"status":status}))
  def get_processes(self,page,page_limit):
    return self.get("process",json.dumps({"page":page,"page_limit":page_limit}))
  def get_process(self,id):
    return self.get("process/" + id,"")
  def get_lists(self,page,page_limit):
    return self.get("list",json.dumps({"page":page,"page_limit":page_limit}))
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
  def create_user(self,attributes,blacklisted,email,listid):
    return self.post("user",json.dumps({"attributes":attributes,"blacklisted":blacklisted,"email":email,"listid":listid}))
  def delete_user(self,id):
    return self.delete("user/" + id,"")
  def update_user(self,id,attributes,blacklisted,listid,listid_unlink):
    return self.put("user/" + id,json.dumps({"attributes":attributes,"blacklisted":blacklisted,"listid":listid,"listid_unlink":listid_unlink}))
  def import_users(self,url,listids,notify_url,name):
    return self.post("user/import",json.dumps({"url":url,"listids":listids,"notify_url":notify_url,"name":name}))
  def export_users(self,export_attrib,filter,notify_url):
    return self.post("user/export",json.dumps({"export_attrib":export_attrib,"filter":filter,"notify_url":notify_url}))
  def create_update_user(self,email,attributes,blacklisted,listid,listid_unlink,blacklisted_sms):
      return self.post("user/createdituser",json.dumps({"email":email,"attributes":attributes,"blacklisted":blacklisted,"listid":listid,"listid_unlink":listid_unlink,"blacklisted_sms":blacklisted_sms}))
  def get_attributes(self,):
    return self.get("attribute","")
  def get_attribute(self,type):
    return self.get("attribute/" + type,"")
  def create_attribute(self,type,data):
    return self.post("attribute",json.dumps({"type":type,"data":data}))
  def delete_attribute(self,type,data):
    return self.post("attribute/" + type,json.dumps({"data":data}))
  def get_report(self,limit,start_date,end_date,offset,date,days,email):
    return self.post("report",json.dumps({"limit":limit,"start_date":start_date,"end_date":end_date,"offset":offset,"date":date,"days":days,"email":email}))
  def get_folders(self,page,page_limit):
    return self.get("folder",json.dumps({"page":page,"page_limit":page_limit}))
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
  def send_transactional_template(self,id,to,cc,bcc,attr):
    return self.put("template/" + id,json.dumps({"cc":cc,"to":to,"attr":attr,"bcc":bcc}))
  def create_template(self,from_name,name,bat_sent,html_content,html_url,subject,from_email,reply_to,to_field,status):
    return self.post("template",json.dumps({"from_name":from_name,"template_name":name,"bat":bat_sent,"html_content":html_content,"html_url":html_url,"subject":subject,"from_email":from_email,"reply_to":reply_to,"to_field":to_field,"status":status}))
  def update_template(self,id,from_name,name,bat_sent,html_content,html_url,subject,from_email,reply_to,to_field,status):
    return self.put("template/" + id,json.dumps({"from_name":from_name,"template_name":name,"bat":bat_sent,"html_content":html_content,"html_url":html_url,"subject":subject,"from_email":from_email,"reply_to":reply_to,"to_field":to_field,"status":status}))
  def get_senders(self,option):
    return self.get("advanced",json.dumps({"option":option}))
  def create_sender(self,sender_name,sender_email,ip_domain):
    return self.post("advanced",json.dumps({"name":sender_name,"email":sender_email,"ip_domain":ip_domain}))
  def update_sender(self,id,sender_name,sender_email,ip_domain):
    return self.put("advanced/" + id,json.dumps({"name":sender_name,"email":sender_email,"ip_domain":ip_domain}))
  def delete_sender(self,id):
    return self.delete("advanced/" + id,"")