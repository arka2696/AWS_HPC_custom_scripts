
# Summary: Securing AWS CLI Credentials on a Shared Computer

When using a shared computer to upload files to AWS S3, it’s important to protect AWS credentials from unauthorized access, modification, or deletion. Here’s a comprehensive guide on securing credentials and managing multiple profiles.

## 1. Restrict File Permissions
One effective way to prevent unauthorized modification or deletion of AWS CLI profiles is to use Windows file permissions on the `credentials` and `config` files.

**Steps:**
- Navigate to `%USERPROFILE%\.aws`.
- Right-click on the `credentials` file and select **Properties**.
- In the **Security** tab, click **Edit** to adjust permissions.
- Grant **Read & Execute** permissions to users who need to use the profile but shouldn't modify it. Remove **Write** permissions as necessary.
- Repeat these steps for the `config` file.

## 2. Temporarily Use Environment Variables
Rather than storing permanent credentials, each user can set AWS credentials as environment variables only for their session. This prevents credentials from persisting on the machine.

**Example Commands in Command Prompt:**
```cmd
set AWS_ACCESS_KEY_ID=your_access_key_id
set AWS_SECRET_ACCESS_KEY=your_secret_access_key
```
After uploading files, clear the environment variables with:
```cmd
set AWS_ACCESS_KEY_ID=
set AWS_SECRET_ACCESS_KEY=
```

This method ensures credentials are only available temporarily, limiting the risk of exposure.

## 3. Using AWS CLI Profiles for Each User
AWS CLI profiles can isolate credentials by storing them under unique profile names in the `credentials` file.

**Setting Up a Profile:**
```cmd
aws configure --profile username
```

**Using a Profile for Uploads:**
```cmd
aws s3 cp yourfile.txt s3://yourbucket --profile username
```

To list all configured profiles, use:
```cmd
aws configure list-profiles
```

## 4. Deleting a User Profile
To delete a profile, manually remove the profile’s section in both `credentials` and `config` files located in `%USERPROFILE%\.aws`.

1. Open `credentials` with:
   ```cmd
   notepad %USERPROFILE%\.aws\credentials
   ```
2. Find and delete the profile’s section.
3. Repeat these steps in `config` if the profile is defined there.

Alternatively, use file permissions to limit users' ability to modify or delete profiles.

## 5. Use AWS SSO or IAM Roles with Temporary Credentials
If available, using AWS Single Sign-On (SSO) or IAM roles with `aws sts assume-role` enables users to work with temporary credentials instead of storing access keys on the machine.

- **AWS SSO**: Users log in via a web portal, receiving temporary credentials without permanently storing them.
- **IAM Assume Role**: Users assume a role for temporary credentials by running:
  ```cmd
  aws sts assume-role --role-arn arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME --role-session-name "sessionName"
  ```
  This method reduces credential exposure and enhances security.

## 6. Automate Credential Management with Scripts
Using a script that prompts users for their credentials, applies them for a session, and clears them afterward can further secure the setup. This ensures credentials don’t persist on the machine.

---

By combining these methods, you can secure AWS CLI credentials on a shared environment, helping to prevent unauthorized access and maintain credential integrity.
